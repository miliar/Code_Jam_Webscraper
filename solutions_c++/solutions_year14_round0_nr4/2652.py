#include <fstream>
#include <algorithm>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int t;

void prs(int caseNum)
{
	int N;
	in >> N;
	double naomi[1001] = {0,};
	double ken[1001] = {0,};

	int warScore = 0;
	int deceitScore = 0;
	int visit[1001] = {0,};
	int i, j;
	
	for(i=0; i<N; i++){
		in >> naomi[i];
	}
	for(i=0; i<N; i++){
		in >> ken[i];
	}
	
	for(i=0; i<N; i++){
		for(j = i+1; j<N; j++){
			if(naomi[i] > naomi[j]){
				double temp;
				temp = naomi[i];
				naomi[i] = naomi[j];
				naomi[j] = temp;
			}
		}
	}

	for(i=0; i<N; i++){
		for(j = i+1; j<N; j++){
			if(ken[i] > ken[j]){
				double temp;
				temp = ken[i];
				ken[i] = ken[j];
				ken[j] = temp;
			}
		}
	}
	for(i=0; i<N; i++){
		int idx = -1;  
		
		for(j=0; j<N; j++){
			if(naomi[i] < ken[j] && visit[j] == 0){
				idx = j;
				break;
			}
		}
		if(idx == -1){
			for(j=0; j<N; j++){
				if(visit[j] == 0){
					visit[j] = 1;
					warScore++;
					break;
				}
			}
			
		}else{
			visit[idx] = 1;
		}
	}
	int naomiMin = 0;

	
	for(i=0; i<N; i++){
		for(j=0; j<N-i; j++){
			if(naomi[j+naomiMin]<ken[j]){
				break;
			}
		}
		if(j == N-i){
			deceitScore++;
		}else{
			naomiMin++;
		}
	}
	out << "Case #"<<caseNum<<": "<<deceitScore<<' '<<warScore<<endl;
}

int main()
{
	in >> t;

	for(int i=0; i<t; i++){
		prs(i+1);
	}
	in.close();
	out.close();
	return 0;
}