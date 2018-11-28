#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<vector<int> > vii;
typedef pair<int,int> pii;
#define endl '\n'
#define rep(i,a,b) for(int i=a;i<b;++i)
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	FILE *fin=freopen("a2.txt","r",stdin);
	assert(fin!=NULL);
	FILE *fout=freopen("ans.txt","w",stdout);
ll x,t,n;
	cin>>t;
	bool b[10];
	for(ll l=1;l<=t;++l){
		cin>>n;
		if(n==0){cout<<"Case #"<<l<<": "<<"INSOMNIA"<<endl;continue;}
		for(ll k=0;k<10;++k)b[k]=false;
		ll i=1;
		while(true){
			x=i*n;
			while(x>0){
				b[x%10]=true;
				x/=10;
			}ll flag=1;
				for(ll k=0;k<10;++k){if(!b[k])flag=0;}
				if(flag==1){cout<<"Case #"<<l<<": "<<i*n<<endl;break;}
			++i;	
		}
	}
	return 0;
}
