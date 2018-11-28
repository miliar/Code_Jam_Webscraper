#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>
#include <iomanip> 
#include <sstream>

using namespace std;

#define TRY
//#define SMALL
//#define LARGE

void Solve();
long long  f[11];
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
{if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

string TenToTwo(int p, int dit){
	string s="";
	while(p!=0){
		s+=('0'+p%2);
		p=p/2;
	}
	int len=dit-s.length();
	while(len>0){s+='0';len--;}
	reverse(s.begin(),s.end());
	return s;
}

void Divide(int N){
	long long tmp;
	for(long long  i=2;i<=10;i++){
		tmp=i*i;
		tmp=tmp*tmp;
		tmp=tmp*tmp;
		if(N==32) tmp=tmp*tmp;
		tmp+=1;
		f[i]=tmp;
	}
}
void main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	freopen("C-large.txt","wt",stdout);
	//freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.txt","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.txt","wt",stdout);
#endif
	int Numcase;
	cin>>Numcase;
	for(int test=1;test<=Numcase;test++)
	{
		cout<<"Case #"<<test<<": ";
		cout<<endl;
		Solve();
	}
}

void Solve(){
	int N,J;
	cin>>N>>J;
	string a,b,ans;
	Divide(N);
	for(int i=0;i<J;i++){
		a = TenToTwo(i,N/2-2);
		b = "1" + a + "1";
		ans = b+b;
		cout<<ans;
		for(int k=2;k<=10;k++){
			cout<<" "<<f[k];
		}
		cout<<endl;
	}
}

