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
#define MOD 1000000007
#define total 500005
#define M 1000000000001
#define NIL 0
#define EPS 1e-5
#define INF (1<<28)
typedef unsigned long long int uint64;
typedef long long int int64;
int64 gcd(int64 x,int64 y){
	if(y==0)
	return x;
	return gcd(y,x%y);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,n;
	int64 p,q;
	cin>>t;
	string s;
	for(int cas=1;cas<=t;cas++){
		cout<<"Case #"<<cas<<": ";
		cin>>s;
		p=0,q=0;
		for(i=0;i<s.length();i++){
			if(s[i]=='/')
			break;
			p=p*10+((int(s[i]))-48);
		}
		for(j=i+1;j<s.length();j++){
			q=q*10+((int(s[j]))-48);
		}
		int64 x=gcd(p,q);
		p=p/x;
		q=q/x;
		//cout<<p<<" "<<q<<endl;
		double num=1;
		while(num<q){
			num*=2;
		}
		if(num!=q){
			cout<<"impossible"<<endl;
			continue;
		}
	double tmp=p/(q*1.0);
	double chck=1;
	for(i=0;i<60;i++){
		if(tmp<=chck&&tmp>=(chck/2))
		break;
		chck/=2;
	}
			cout<<i+1<<endl;
		}
	fclose(stdout);
	return 0;
}
