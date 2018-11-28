#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <vector>
#include <math.h>
#include <iomanip>
#include <map>      // std::pair

#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SIZE(v) ((int)(v).size())
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
typedef long long ll;
typedef std::pair<ll,ll> PII;
//typedef vector<PII> VPII;
using namespace std;

unsigned __int64 r,t,k,ku,kl,kk;

int len(unsigned __int64 x){
	int leng=0;
do
{
    leng++;
}while(x /= 10);
return leng;
}
bool func(unsigned __int64 kk){
	unsigned __int64 p=r+2*kk,x,x1,x2,y;
	x1=(p-r+2);
	x2=(r+1+p);
	y=2*t;
	int l1=len(x1);
	int l2=len(x2);
	if (l1+l2-1>len(2*t))	return false;
	return (x1*x2<=y);
}

void solve(){
	cin>>r>>t;
	//k=(unsigned __int64)sqrt((double)(2*t+r*r-r-2)) + 5;
	k=r+t;
	ku=(k+1)/2;
	kl=0;
	while(kl<ku){
		kk=(ku+kl)/2;
		if (func(kk)){
			if (!func(kk+1))	{
				kl=kk;
				break;
			}
			else	kl=kk+1;
		}
		else	ku=kk-1;
	}
	cout<<kl+1<<endl;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin>>t;
	FOE(i,1,t){
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;

}	