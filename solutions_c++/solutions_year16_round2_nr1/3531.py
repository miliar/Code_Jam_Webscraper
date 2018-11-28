#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 100005
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>

using namespace std;

int mark[500];

string have[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool valid(){
	
	bool flag=0;
	
	for(int j=0;j<10;j++){
		int right[500];
		
		for(int k='A';k<='Z';k++) right[k]=0;
				
		for(int k=0;k<have[j].length();k++){
			right[have[j][k]]++;
		}
			
		bool ok=0;
				
		for(int k='A';k<='Z';k++){
			if(right[k]<=mark[k]) continue;
			ok=1;
		}
		
		if(ok) continue;
		
		flag=1;
		
		for(int k='A';k<='Z';k++){
			mark[k]-=right[k];
		}
		
		int ret=0;
		if(valid()) ret=1;
		else flag=0;
		
		for(int k='A';k<='Z';k++){
			mark[k]+=right[k];
		}
		
		if(ret) return ret;
	}
	
	if(!flag) for(int k='A';k<='Z';k++) if(mark[k]!=0) return 0;
	return 1;
}

int main(){
	
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A1.out","w",stdout);
	
	//freopen("A-large.in","r",stdin);
	//freopen("A2.out","w",stdout);
	
	int tt;
	sd(tt);
	for(int i=1;i<=tt;i++){
		
		string in;
		cin>>in;
		
		for(int j='A';j<='Z';j++) mark[j]=0;
		
		int l=in.length();
		for(int j=0;j<l;j++) mark[in[j]]++;
		
		string ans;
		
		for(int j=0;j<10;j++){
			int p=1;
			while(p){
				int right[500];
				
				for(int k='A';k<='Z';k++) right[k]=0;
				
				for(int k=0;k<have[j].length();k++){
					right[have[j][k]]++;
				}
				
				for(int k='A';k<='Z';k++){
					if(right[k]<=mark[k]) continue;
					p=0;
				}
				
				if(p){
					for(int k='A';k<='Z';k++){
						mark[k]-=right[k];
					}
					if(valid()) ans+=char(j+'0');
					else{
						for(int k='A';k<='Z';k++){
							mark[k]+=right[k];
						}
						p=0;
					}
				}
			}
		}
		
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
