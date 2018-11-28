#include <bits/stdc++.h>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define repb(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int main(){
	ifstream fin("in.txt");
	ofstream fout("out1.txt");
	
	int t;
	cin>>t;

	rep(x,0,t){
		string s;
		cin>>s;
		int p=0,m=0;

		rep(i,0,s.size()){
			if(i && s[i-1]==s[i]) continue;
			if(s[i]=='+') p++;
			else m++;
		}

		int a,f=0,g=0;
		if(m>(m+p)/2){
			a=p; g=1;
			if(s[0]=='+') f=1;
		}else{
			a=m;
			if(s[0]=='-') f=1;
		}

		int ans=2*a-f+g;

		fout<<"Case #"<<x+1<<": "<<ans<<endl;
	}
}