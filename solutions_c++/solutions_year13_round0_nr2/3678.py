#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(void){

	int N;
	long long*a;
	long long*b;
	int i;
	
	ifstream fin;
	fin.open("B-large.in",ios_base::in);
	ofstream fout;
	fout.open("output.txt",ios_base::out);

	fin>>N;
	for(int test=0;test<N;test++){

		int N,M;
		fin>>N>>M;
		int i,j,k;
		int amount[100] = {0};
		int **data = new int*[N];
		for(i=0;i<N;i++) data[i] = new int[M];
		int maxHeight = -1;
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				fin>>data[i][j];
				amount[data[i][j]-1]++;
				if(data[i][j] > maxHeight) maxHeight = data[i][j];
			}
		}

		int curHeight = maxHeight;
		bool possible = true;
		bool **visited = new bool*[N];
				for(i=0;i<N;i++) visited[i] = new bool[N];
	
				for(i=0;i<N;i++){
					for(j=0;j<M;j++){
						visited[i][j] = false;
					}
				}

		while(curHeight > 1 && possible){
			
			int total = 0;
			
			if(amount[curHeight-2] > 0){

				for(j=0;j<M;j++){
					int max = -1;
					for(i=0;i<N;i++) if(data[i][j] > max) max = data[i][j];
					int curTotal = 0;
					if(max <= curHeight-1){
						for(i=0;i<N;i++){
							if(!visited[i][j]){
								if(data[i][j] == curHeight-1){
									total++;
									visited[i][j] = true;
									curTotal++;
								}
							}
							else if(data[i][j] >= curHeight){
								total -= curTotal;
								break;
							}
						}
					}
				}

				for(i=0;i<N;i++){
					int max = -1;
					for(j=0;j<M;j++)
						if(data[i][j] > max) max = data[i][j];
					int curTotal = 0;
					if(max <= curHeight-1){
						for(j=0;j<M;j++){
								if(!visited[i][j]){
									if(data[i][j] == curHeight-1){
										total++;
										visited[i][j] = true;
									}
								}
								else if(data[i][j] >= curHeight){
									total -= curTotal;
									break;
								}
							}
						}
					}

				if(total != amount[curHeight-2]){
					possible = false;
					break;
				}
			}
			curHeight--;
		}
		if(possible) fout<<"Case #"<<test+1<<": YES"<<endl;
		else fout<<"Case #"<<test+1<<": NO"<<endl;
		
	}

	fin.close();
	fout.close();



}