#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<=(int)(m);i++)
using namespace std;
bool pal(int n){int tm=n,r=0;while(n>0){r=r*10+n%10;n/=10;}return (tm==r);}
int T,A,B;
int main(){
freopen("C-small-attempt0.in","rt",stdin);
freopen("C-small.out","wt",stdout);
cin >> T;
rep(tt,T){
	cin >>A>>B;
	int sa=ceil(sqrt(A)),sb=floor(sqrt(B)),count=0;
	rep2(i,sa,sb){
		if(pal(i))if(pal(i*i))count++;
		}
	cout<<"Case #"<<(tt+1)<<": "<<count<<"\n";
	}
}
