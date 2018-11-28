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

vector<ll> dic;

bool isPal(ll x){
	string str = "";
	while(x>0){
		char c='0'+x%10;
		x=x/10;
		str=c+str;
	}
	FOR(i,0,str.length()){
		if (str[i]!=str[str.length()-1-i]){
			return false;	
		}
	}
	return true;
}

void init(){
	ll d[8]={0};
	for (ll i=1;i<=9999;i++){
		ll q,j=i,res=i;
		while (j>0){
			q=j%10;
			j=j/10;
			res=res*10+q;
		}
		if (isPal(res*res))	dic.push_back(res);

		j=i;res=i;
		j=j/10;
		while (j>0){
			q=j%10;
			j=j/10;
			res=res*10+q;
		}
		if (isPal(res*res))	dic.push_back(res);
	}
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("d.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	init();

	ll t,a,b;
	cin>>t;
	FOR(tt,0,t){
		cin>>a>>b;
		double aa=(int)sqrt((double)a)-1;
		double bb=(int)sqrt((double)b)+1;
		ll k,sum=0;
		for (int i=0;i<(int)dic.size();i++){
			k=dic[i];
			if (k*k>=a && k*k<=b){
				//if (isPal(k)&&isPal(k*k))
				{
					//cout<<k<<endl;
					sum++;
				}
			}
		}
		cout<<"Case #"<<tt+1<<": "<<sum<<endl;
	}

	return 0;

}