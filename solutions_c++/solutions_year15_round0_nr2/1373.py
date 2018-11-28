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
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

priority_queue<int>p,q;


int chck(int val){
	int add=0;
	while(1){
		int x=p.top();
		p.pop();
		if(x==val)
		return add+val;
		p.push(max(val,x-val));
		add++;
	}
}

int main(){
	int t,n,i,val;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>n;
		p=priority_queue<int>();
		q=priority_queue<int>();
		
		for(i=0;i<n;i++){
			cin>>val;
			p.push(val);
			q.push(val);
		}
		int fin=1e9;
		for(int ans=1;ans<=p.top();ans++){
			fin=min(fin,chck(ans));
			p=q;
		}
		printf("%d\n",fin);
	}
	fclose(stdout);
	return 0;
}
