#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//map<ll,ll>M;
ll v[2000000];
queue<ll>Q;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int T,cse;
	ll n,c,i,nn,j,frt,tmp;
	scanf("%d",&T);
	for(cse=1;cse<=T;cse++)
	{
		scanf("%I64d",&n);
		//M.clear();
		memset(v,0,sizeof v);
		while(!Q.empty())Q.pop();
		Q.push(1LL);
		//M.insert(map<ll,ll>::value_type(1LL,1LL));
		v[1]=1LL;
		while(!Q.empty())
		{
			frt=Q.front();
			if(frt==n)
			{
				//c=M[frt];
				c=v[frt];
				break;
			}
			Q.pop();
			tmp=frt+1LL;
			if(v[tmp]==0LL/*M.find(tmp)==M.end()*/)
			{
				//M.insert(map<ll,ll>::value_type(tmp,M[frt]+1LL));
				v[tmp]=v[frt]+1LL;
				Q.push(tmp);
			}
			j=frt;
			tmp=0LL;
			while(j)
			{
				tmp=tmp*10LL+j%10LL;
				j/=10LL;
			}
			//if(tmp<=frt)continue;
			if(v[tmp]==0LL/*M.find(tmp)==M.end()*/)
			{
				//M.insert(map<ll,ll>::value_type(tmp,M[frt]+1LL));
				v[tmp]=v[frt]+1LL;
				Q.push(tmp);
			}
		}
		printf("Case #%d: %I64d\n",cse,c);
	}
	return 0;
}
