#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)

double v,x,t1,t2,r1,r2,c1,c2;
double check()
{
	if(c1==c2 && c1==x)
	{
		return v/(r1+r2);
	}
	if(c1==c2){
		return -1;
	}
	t1 = v*(c2-x)/((c2-c1)*r1);
	t2= v*(c1-x)/((c1-c2)*r2);
//	cout<<"here"<<endl;
	if(t1<0 || t2<0)return -1;
	return max(t1,t2);
}
int main() {
	// your code goes here
	int cases;
	cin>>cases;
	int n;
	for(int case_t = 1; case_t<=cases;++case_t)
	{
		cout<<"Case #"<<case_t<<": ";
		cin>>n;
		cin>>v>>x;
		cin>>r1>>c1;
		if(n==1)
		{
			if(x==c1)
			{
				cout<<v/r1<<endl;
			}
			else
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
			continue;
		}
		cin>>r2>>c2;
		double ans = check();
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
		else printf("%.8lf\n",ans);
	}
	return 0;
}