/* attention to overflow */
#include <bits/stdc++.h>

#define dump(x) cerr<< #x << " = " << x <<endl
#define ALL(container) (container).begin(),(container).end()

using namespace std;
const int INF = 1 << 25;
void io() { cin.tie(0); ios::sync_with_stdio(false);}
template <class S,class T> ostream& operator<<(ostream& os, const pair <S,T> &s){return os<<'('<<s.first<<','<<s.second<<')';}
/*printf("%.9Lf\n",cf);*/
const int MOD = 1000000007;
const double EPS=1e-8;

string cs(int n){ return "Case #"+to_string(n)+": "; }

//int check(){return ;}
map <int,string> ch;

string max_string(int P,int N){
	if(N==0) return ch[P];
	string a=max_string(P,N-1);
	string b=max_string((P+1)%3,N-1);
	if(a<b) return a+b;
	return b+a;
}

int main() {
	io();

	ch[0]="P";
	ch[1]="R";
	ch[2]="S";

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int N,R,P,S;
		cin>>N>>R>>P>>S;
		int n=R+P+S;
		bool flg=0;
		while(R+P+S>2){
			if(R>=n/4 && P>=n/4 && S>=n/4){
				R-=n/4;P-=n/4;S-=n/4;
				int p=P;
				int r=R;
				int s=S;
				P=r;
				R=s;
				S=p;
			}else{
				flg=1;
				break;
			}
			n/=4;
		}

		if(R==2 || P==2 || S==2) flg=1;

		if(flg){
			cout<<cs(t)<<"IMPOSSIBLE";
			if(t!=T) cout<<endl;
			continue;
		}

		if(R+P+S==2){
			if(R==1&&P==1) R=0;
			else if(S==1&&R==1) S=0;
			else P=0;
		}
		cerr<<P<<R<<S<<endl;
		int val=0;
		if(R==1) val=1;
		if(S==1) val=2;
		cout<<cs(t)<<max_string(val,N);
		if(t!=T) cout<<endl;
	}


	return 0;
}
