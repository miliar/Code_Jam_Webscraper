#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;
#define ll long long
ll gcd ( ll a, ll b )
{
  if ( a==0 ) return b;
  return gcd( b%a, a );
}

ll check_pow(ll num)
{
	ll val=1,i;
	for(i=0;val<num;i++){
		val*=2;
	}
	if(val==num && num!=1) return i;
	else return -1;
}

int main(){
ofstream ofs;
ofs.open("out.txt");
ll t;
cin>>t;
ll numer, denom;
for(ll i=0;i<t;i++){
	scanf("%lld/%lld",&numer, &denom);
	/*ll k=0;	
	ll cnt_numer=0,cnt_denom=0;
	while(inp[k++]!='/'){
		cnt_numer++;
	}
	while(inp[k++]!='\0'){
		cnt_denom++;
	}
	k=0;
	
	while(cnt_numer--){
		numer+=( (inp[k++]-48)*pow(10,cnt_numer));		
	}
	while(cnt_denom--){
		denom+=( (inp[k++]-48)*pow(10,cnt_denom));		
	}
	*/
	//cout<<numer<<" "<<denom<<endl;
	ll g = gcd(denom,numer);
	numer/=g;
	denom/=g;
	ll index = check_pow(denom);
	if(index==-1) {ofs<<"Case #"<<i+1<<": impossible"<<endl;continue;}
	//cout<<g<<endl;
	while(numer>1){
		numer=numer/2;
		denom=denom/2;
	}
	if(numer==1){	
			 index = check_pow(denom);
			if(index==-1) ofs<<"Case #"<<i+1<<": impossible"<<endl;
			else ofs<<"Case #"<<i+1<<": "<<index<<endl;
	}

}
return 0;
}
