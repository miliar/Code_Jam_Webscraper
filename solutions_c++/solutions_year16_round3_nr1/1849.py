#define ll long long
#define mod 1000000007LL
#define F(a,b,c) for(a=b;a<c;a++)
#define Fr(a,b,c) for(a=b;a>=c;a--)
#define pf printf
#define sfd(a) scanf("%d",&a)
#define sfdd(a,b) scanf("%d%d",&a,&b)
#define sfl(a) scanf("%lld",&a)
#define sfll(a,b) scanf("%lld%lld",&a,&b)
#define pfd(a) printf("%d",a)
#define pfl(a) printf("%lld",a)
#define sf scanf
#define line printf("\n")
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define let(x,a) __typeof(a) x(a)
#define forall(it,v) for(it=v.begin();it!=v.end();it++)
int main(){
int t;
sfd(t);
int k=1;
while(k<=t){
	priority_queue<pair<int,int> > pr;
	int n,i,a[28];
	sfd(n);
	F(i,0,n)
		sfd(a[i]),pr.push(mp(a[i],i));
	pf("Case #%d:",k);
	while(!pr.empty()){
		if(pr.size()>2){
			pair<int,int> p=pr.top();
			pr.pop();
			if(p.first>1)
			pr.push(mp(p.first-1,p.second));
			pf(" %c",p.second+65);	
		}
		else if(pr.size()==2){
			pair<int,int> p=pr.top();
			pr.pop();
			pair<int,int> p2=pr.top();
			pr.pop();
			if(p.first==p2.first){
				pf(" %c%c",p.second+65,p2.second+65);
				if(p.first>1)
					pr.push(mp(p.first-1,p.second));
				if(p2.first>1)
					pr.push(mp(p2.first-1,p2.second));
				}
			else{
				if(p.first>1)
			pr.push(mp(p.first-1,p.second));
			pr.push(p2);
			pf(" %c",p.second+65);
			}
		}
		
	}
	line;
	k++;
}
return 0;
}
