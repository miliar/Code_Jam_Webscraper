#include<iostream>
#include<fstream>
using namespace std;
void main(){
	int M,N,T;
	int rec[110][110];
	ifstream cin("B-small-attempt1.in");
	ofstream cout("2013gcj_qr_B(3).out");
	cin >> T;
	for(int i = 0; i < T; i++){
		bool flag = true;
		cout << "Case #"<<i+1<<": ";
		cin >> N >> M;
		for(int j = 0; j< N; j++)
			for(int k = 0; k < M; k++)
				cin >> rec[j][k];
		if(N == 1 || M == 1){cout << "YES" << endl;continue;}
		/*
		for(int j = 0; j < N; j++){
			for(int k = 0; k < M; k++){
				if(j == 0&& k == 0 && !(rec[j][k] == rec[j][M-1] || rec[j][k] == rec[N-1][k])){flag = false;break;}
				else if(j == 0 && !(rec[j][k] == rec[j][0] || rec[j][k] == rec[N-1][k])){flag = false;break;}
				else if(k == 0 && !(rec[j][k] == rec[j][M-1]||rec[j][k] == rec[0][k])){flag = false;break;}
				else if(!(rec[j][k] == rec[0][k] || rec[j][k] == rec[j][0])){flag = false;break;}
			}
			if(!flag){cout << "NO"<<endl;break;}
		}
		if(!flag)continue;
		*/
		for(int j = 0; j < N; j++){
			for(int k = 0; k < M; k++){
				bool colbig=false,rowbig=false,equalorless=false;
				for(int l = 0;l < N; l++){
					if(l == j)continue;
					if(rec[l][k] == rec[j][k])equalorless = true;
					else if(rec[l][k] > rec[j][k])colbig = true;
				}
				for(int l = 0;l < M; l++){
					if(l == k)continue;
					if(rec[j][l] <= rec[j][k])equalorless = true;
					else if(rec[j][l] > rec[j][k])rowbig = true;
				}
				if(rowbig&&colbig||!equalorless){flag = false;break;}
			}
			if(!flag){cout << "NO" << endl;break;}
		}
		if(flag)cout << "YES" << endl;
	}
	system("pause");
}