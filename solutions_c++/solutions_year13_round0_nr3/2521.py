#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define pb push_back
typedef long long tint;
const int MAX_POT=10;
tint pot[MAX_POT];

int dig(tint n){
	int res = 0;
	while(n>0){
		res++;
		n/=10;
	}
	return res;
}

tint reverse(tint n){
	tint res = 0;
	while(n>0){
		res*=10;
		res+=n%10;
		n/=10;
	}
	return res;
}

bool isPalindrome(tint n){
	tint m =reverse(n);
	if(m==n)return true;
	return false;
}

int main(){
	int t; cin>>t; int caso = 0;
	pot[0]=1;
	forn(i,MAX_POT-1)pot[i+1]=10*pot[i];
	vector<tint>v, vant;
	forn(a,10000){
		tint num = a;
		//cout<<num<<' ';
		num*=pot[dig(a)];
		//cout<<num<<' ';
		num+=reverse(a);
		//cout<<num<<endl;
		if(isPalindrome(num*num)){v.pb(num*num); vant.pb(num);}
		
		forn(b,10){
			num=a;
			//cout<<num<<' ';
			num*=pot[dig(a)+1];
			//cout<<num<<' ';
			num+=b*pot[dig(a)];
			//cout<<num<<' ';
			num+=reverse(a);
			//cout<<num<<endl;
			if(isPalindrome(num*num)){v.pb(num*num); vant.pb(num);}
		}
	}
	
	sort(v.begin(), v.end());
	sort(vant.begin(), vant.end());
	//forn(i,v.size())cout<<vant[i]<<' '<<v[i]<<endl;

	while(t>0){
		t--; caso++;
		tint a, b; cin>>a>>b;
		int res = 0;
		forn(i,v.size())if(a<=v[i] && v[i]<=b)res++;
		printf("Case #%d: %d\n", caso, res);
	}
	
}
