#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back 
queue<int> q;
vector<int> v[1000005];
int flip(int x){
	int r;int a=0;
	while(x>0){
        r=x%10;
        a=10*a+r;
        x/=10;
	}
	return a;
}
int n,c=1;
int ans[1000005],vis[1000005];
int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
      q.push(1);
      vis[1]=1;
     	ans[1]=1;
       	while(!q.empty()){
		int g=q.front();
		if(g>1000000){q.pop();continue;}
		q.pop();
		//if(g==n){cout<<"Case #"<<c<<": "<<ans[g]<<'\n';c++;goto l;}
		v[g].pb(g+1);
		if(flip(g)<=1000000)
		v[g].pb(flip(g));
		for(int i=0;i<v[g].size();i++){
		if(!vis[v[g][i]]){
			vis[v[g][i]]=1;
		      ans[v[g][i]]=ans[g]+1;
		      q.push(v[g][i]);
		}
      }
     }
     int t;
     cin>>t;
    while(t--){
     	cin>>n;
     cout<<"Case #"<<c<<": "<<ans[n]<<'\n';c++;	

 }
return 0;
}

