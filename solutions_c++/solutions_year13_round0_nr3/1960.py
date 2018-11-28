///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define formn(i,m,n) for(int i=m;i<(int)n;i++)
#define dformn(i,m,n) for(int i=n-1;i>=m;i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

tint res;
tint lo,hi;

///Dígitos de un número n.
vector<int> digitos(tint n){
    vector<int> res;
    while(n>0){
        res.push_back(n%10);
        n/=10;
    }
    reverse(res.begin(),res.end());
    return res;
}

bool isPal(tint n){
	vector<int> d=digitos(n);
	forn(i,d.size()) if(d[i]!=d[d.size()-1-i]) return false;
	return true;
}

void backtrack(tint n){
	if(n*n>hi) return;
	if(lo<=n*n && n*n<=hi && isPal(n) && isPal(n*n)) res++;
	forn(d,4){
		if(n==0 && d==0) continue;
		backtrack(n*10+d);
	}
}

int main(){
//freopen("Clarge.txt","r",stdin);
freopen("CinputLarge.txt","r",stdin);
freopen("CoutputLarge.txt","w",stdout);
	int TC;cin>>TC;
	formn(tc,1,TC+1){
		cin>>lo>>hi;
		res=0;
		backtrack(0);
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
    return 0;
}
