#include<iostream>
#include<string>
using namespace std;


char map[6][6];
int cnt=1;

void count_r(int i, int j) {
	char cur = map[i][j];
	if(cur == 'a' || cur == '.') return;
	
	if(map[i][j+1] == cur || map[i][j+1] == 'T') {
		cnt++;
		count_r(i, j+1);
	}	
}

void count_c(int i, int j) {
	char cur = map[i][j];
	if(cur == 'a' || cur == '.') return;
	
	if(map[i+1][j] == cur || map[i+1][j] == 'T') {
		cnt++;
		count_c(i+1, j);
	}
}

void count_d(int i, int j) {
	char cur = map[i][j];
	if(cur == 'a' || cur == '.') return;
	
	if(map[i+1][j+1] == cur || map[i+1][j+1] == 'T') {
		cnt++;
		count_d(i+1, j+1);
	}
}

void count_d2(int i, int j) {
	char cur = map[i][j];
	if(cur == 'a' || cur == '.') return;
	
	if(map[i+1][j-1] == cur || map[i+1][j-1] == 'T') {
		cnt++;
		count_d2(i+1, j-1);
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n,a, all=0;
	char ret;
	cin>>n;
	bool flag = false;

	string ans[]= {"X won", "O won", "Draw", "Game has not completed"};

	for(int cs=1; cs<=n; cs++) {
		flag = false;
		cnt = 1;

		for(int i=0; i<6; i++) 
			for(int j=0; j<6; j++) { 
				if(i==0 || j==0 || i==5 || j==5) map[i][j] ='a';
				else cin>>map[i][j];

				if(map[i][j] == '.') flag = true; //아직 승부 안남
			}


		for(int i=1; i<5; i++) {
			for(int j=1; j<5; j++) { 

				count_r(i,j);
				if(cnt == 4) {
					ret = map[i][j];
					goto OMG;
				}
				cnt = 1;

				count_c(i,j);
				if(cnt == 4) {
					ret = map[i][j];
					goto OMG;
				}
				cnt = 1;

				count_d(i,j);
				if(cnt == 4) {
					ret = map[i][j];
					goto OMG;
				}
				cnt = 1;

				count_d2(i,j);
				if(cnt == 4) {
					ret = map[i][j];
					goto OMG;
				}
				cnt = 1;

			}
		}

		if(flag == true)
			ret = 'N';
		else
			ret = 'D';

OMG:
		switch(ret) {
			case 'X': a =0; break;
			case 'O': a =1; break;
			case 'D': a =2; break;
			case 'N': a =3; break;
		}

		cout<<"Case #"<<cs<<": "<<ans[a]<<endl;
	}

	return 0;
}



//for(int i=1; i<=4; i++) {
//			for(int j=1; j<=4; j++) {
//				cout<<map[i][j];
//			}
//			cout<<endl;
//		}


	/*	for(int i=0; i<6; i++) {
			for(int j=0; j<6; j++) {
				cout<<map[i][j];
			}
			cout<<endl;
		}*/