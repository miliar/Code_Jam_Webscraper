#include <bits/stdc++.h>

using namespace std;
#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

string red(string S){
	string f="";
	f+=S[0];
	FORAB(i,1,SZ(S)-1){
		if(S[i]!=S[i-1]){
			f+=S[i];
		}
	}
	return f;
}

int main(){
	LL t,test;
	cin >> t;
	FORN(test,t){
		LL n;
		vector < string > A;
		string reduced="",S;
		int not_pos=0;
		vector < vector < int > > mn_vec;
		cin >> n;
		FORN(i,n){
			cin >> S;
			if(reduced==""){
				reduced=red(S);
			}
			else{
				if(reduced!=red(S)){
					not_pos=1;
				}
			}
			A.PB(S);
		}
		if(not_pos==1){
			cout << "Case #" << test+1 << ": Fegla Won" << endl;
			continue;
		}
		FORN(i,SZ(A)){
			vector < int > temp;
			LL cnt=1;
			FORAB(j,1,SZ(A[i])-1){
				if(A[i][j]==A[i][j-1]){
					cnt++;
				}
				else{
					temp.PB(cnt);
					cnt=1;
				}
			}
			temp.PB(cnt);
			// FORN(j,SZ(temp)){
			// 	cout << temp[j] << " ";
			// }cout << endl;
			mn_vec.PB(temp);
		}
		LL ans=INT_MAX;
		FORN(i,SZ(A)){
			LL t_ans=0;
			FORN(j,SZ(A)){
				FORN(k,SZ(mn_vec[j])){
					t_ans+=abs(mn_vec[j][k]-mn_vec[i][k]);
				}
			}
			ans=min(ans,t_ans);
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
	}
	return 0;
}