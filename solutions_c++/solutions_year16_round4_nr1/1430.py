#include <iostream>
#include <string>
#include <bitset>
#include <math.h>
#include <set>
#include <algorithm>
using namespace std;

int index = 1;
char res[5000] = {'0'};
char winner(char i ,char j)
{
	if (i==j) return 'N';
	if (i == 'P' && j == 'R') return 'P';
	if (i == 'R' && j == 'P') return 'P';
	if (i == 'P' && j == 'S') return 'S';
	if (i == 'S' && j == 'P') return 'S';
	if (i == 'S' && j == 'R') return 'R';
	if (i == 'R' && j == 'S') return 'R';
}

bool iffinish(string str, int N){
	while(N--){
		string tmp = "";
		for (int i=0;i<(1<<(N));i++){
			char l = str[i*2];
			char r = str[i*2+1];
			char tt = winner(l,r);
//			cout << l << " " << r << endl;
			if (tt == 'N') return false;
			tmp += tt;
		}
		str = tmp;
//		cout << "str = " << str << endl;
	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	while(T--){
		int N,R,P,S;
		string str="";
		cin >> N >> R >> P >> S;
		int playNUm = 1<<N;
		int thod = 2<<(N-1);
		int counts[5000] = {0,2,1,3}; // 8 n=2
		int now_N = 2;
		int tmps[5000] = {0};
		if (R>=thod || P>=thod || S>=thod) str = "IMPOSSIBLE";
		else if (!(R && P && S) && N==2) str = "IMPOSSIBLE";
		else if (N == 1){
			while(P--) str += 'P';
			while(R--) str += 'R';
			while(S--) str += 'S';
		}
		else if (N == 2){
			if (R==2) str = "PRRS";
			if (P==2) str = "PRPS";
			if (S==2) str = "PSRS";
		}
//		else if (N == 3){
//			if (R==2) str = "PRPSPSRS";
//			if (P==2) str = "PRRSPSRS";
//			if (S==2) str = "PRPSPRRS";
//		}
		else{
			int _N = N;
			while(_N > 2){
				int x = 1 << (now_N);
//				cout << "x=" << x << endl;
				for (int i=0;i<(1<<(now_N));i++){
					tmps[i*2] = counts[i];
					tmps[i*2+1] = counts[i]+ x;
				}
				for (int i=0;i<(1<<(now_N+1));i++){
					counts[i] = tmps[i];
//					cout << counts[i] << endl;
				}
				now_N ++;
				_N --;
			}
			for (int i=0;i<(1<<(N));i++){
				if (P-->0)
					res[counts[i]] = 'P';
				else if (R-->0)
					res[counts[i]] = 'R';
				else if (S-->0)
					res[counts[i]] = 'S';
			}
			for (int i=0;i<(1<<(N));i++){
				str += res[i];
			}
//			cout << "str = " << str << endl;
			if (!iffinish(str, N)) str = "IMPOSSIBLE";
		}
		cout << "Case #" << index++ << ": " << str << endl;
	}
	return 0;
}