#include<bits/stdc++.h>
#include<ext/rope>
#define f first
#define s second
using namespace std;
using namespace __gnu_cxx;
typedef pair<int,int>par;
string s[10];
multiset<string> ar[10];
int m,n;
int ma,ans2;
void F(int k){
	if(k==m){
		int cnt=0;
		for(int i=0;i<n;i++)
			if(ar[i].empty())return;
		for(int i=0;i<n;i++){
			string now="";
            for(multiset<string>::iterator it=ar[i].begin(),ed=ar[i].end();it!=ed;++it){
				int cn;
				for(cn=0;cn<min(it->length(),now.length());cn++)
					if((*it)[cn]!=now[cn])break;
				cnt+=it->length()-cn;
				now=*it;
				//cout<<*it<<endl;
				}
			}
		cnt+=n;
		if(cnt>ma)ma=cnt,ans2=0;
		if(cnt==ma)ans2++;
		return;
		}
	for(int i=0;i<n;i++){
		ar[i].insert(s[k]);
		F(k+1);
		ar[i].erase(s[k]);
		}
	}
int main(){
	int T,t=0;
	scanf("%d",&T);
	while(T--){t++;
		scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++)
			cin>>s[i];
		ma=0;ans2=0;
		F(0);
		printf("Case #%d: %d %d\n",t,ma,ans2);
		}
    return 0;
    }
