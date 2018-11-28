#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000003
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

int vis[1000005];
int rev(int x){
	vector<int>v;
	while(x){
		int dig=x%10;
		x/=10;
		v.push_back(dig);
	}
	int ret=0;
	for(int i=0;i<v.size();i++)
	ret=ret*10+v[i];
	return ret;
}

int main(){	
	int t,n,i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>n;
		queue<pair<int,int> >q;
		q.push(mp(1,1));
		vis[1]=cas;
		pair<int,int>tmp,tmp1;
		while(!q.empty()){
			tmp=q.front();
			q.pop();
			if(tmp.first==n)
			break;
			tmp1.first=tmp.first+1;
			tmp1.second=tmp.second+1;
			if(tmp1.first<=1000000){
				if(vis[tmp1.first]!=cas){
					vis[tmp1.first]=cas;
					q.push(tmp1);
				}
			}
			tmp1.first=rev(tmp.first);
			tmp1.second=tmp.second+1;
			if(tmp1.first<=1000000){
				if(vis[tmp1.first]!=cas){
					vis[tmp1.first]=cas;
					q.push(tmp1);
				}
			}
		}
		printf("%d\n",tmp.second);
	}
	fclose(stdout);
	return 0;
}
