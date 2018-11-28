#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<set>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
using namespace std;


typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define pb push_back
#define mp make_pair
#define snd second
#define fst first
#define debug printf("--%d--\n",__LINE__)
#define ll long long int


int N, R, P, S;
int T;
int main(void){
	cin >> T;
	for(int casenum=1;casenum<=T;casenum++){
		cin >> N >> R >> P >> S;
		cout << "Case #" << casenum << ": ";
		
		bool orz = false;
		int p = P, s = S, r = R, p2, s2, r2;
		for(int i=0;i<N;i++){
			p2 = (r+p-s)/2;
			s2 = (p+s-r)/2;
			r2 = (s+r-p)/2;
			p = p2;
			s = s2;
			r = r2;
			if (p<0 || s<0 || r<0){
				orz = true;
				break;
			}
		}
		if (orz){
			cout << "IMPOSSIBLE" << endl;
		}else{
			string st = "";
			if (p) st = "P";
			if (s) st = "S";
			if (r) st = "R";
			string st2;
			for(int i=0;i<N;i++){
				st2 = "";
				for(int j=0;j<st.size();j++){
					if (st[j]=='P'){
						st2 += "PR";
					}else if (st[j]=='S'){
						st2 += "PS";
					}else{
						st2 += "RS";
					}
				}
				st = st2;
			}
			
			for(int i=1;i<N;i++){
				int M = 1<<i;
				for(int j=0;j<(1<<(N-1-i));j++){
					string s1 = st.substr(j*2*M,M);
					string s2 = st.substr((j*2+1)*M,M);
					if (s1 > s2){
						st = st.substr(0,j*2*M) + s2 + s1 + st.substr((j+1)*2*M);
					}
				}
			}
			cout << st << endl;
		}
		
	}
	
	return 0;
}
