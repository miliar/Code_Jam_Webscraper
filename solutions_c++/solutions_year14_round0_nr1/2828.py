#include <fstream>

using namespace std;

int t;

ifstream in("input.txt");
ofstream out("output.txt");
void prs(int caseNum)
{
	int i, j;
	int a1[4][4] = {0, };
	int a2[4][4] = {0, };
	int visit[17] = {0,};
	int r1, r2;

	in >> r1;
	
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			in >> a1[i][j];
			if(i==r1-1) visit[a1[i][j]]++;
		}
	}

	in >> r2;

	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			in >> a2[i][j];
			if(i==r2-1) visit[a2[i][j]]++;
		}
	}

	int cnt = 0;
	int card = 0;
	for(i=1; i<=16; i++){
		if(visit[i] == 2){
			card = i;
			cnt++;
		}
	}
	out << "Case #"<<caseNum<<": ";
	if(cnt == 1) out << card << endl;
	else if (cnt > 1) out << "Bad magician!"<<endl;
	else if (cnt == 0) out << "Volunteer cheated!"<<endl;
}
int main()
{
	in >> t;
	for(int i = 0; i<t; i++){
		prs(i+1);
	}
	in.close();
	out.close();
	return 0;
}