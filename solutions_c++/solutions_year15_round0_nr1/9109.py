//set
#include"stdio.h"
#include"iostream"
#include"vector"
#include"string"
#include"string.h"
#include"algorithm"
#include"math.h"
#include"set"
#include"bitset"
#include"map"


#define ABS(a) ((a<0)?(-a):a)
#define MAX(a) ((a<b)?b:a)
#define MIN(a) ((a>b)?b:a)
#define FOR(i,n) for(int i=0;i<n;++i)
#define FORA(a,n) for(int i=a;i<n;++i) 
#define pb push_back
#define MP make_pair

using namespace std;

typedef long long LL; 
typedef unsigned long long ULL;
const double pi=3.141592653589;
const int ten5=100000;

int t,n;
LL sum,rez;
string s;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	cin>>t;
	FOR(i,t)
	{
		cin>>n;
		n++;
		cin>>s;
		n=s.size();
		sum=rez=0;
		FOR(j,n)
		{
			if(j>sum) {rez+=j-sum;sum+=j-sum;}
			sum+=(s[j]-48);
		}
		cout<<"Case #"<<(i+1)<<": "<<rez<<endl;

	}



	return 0;
}

	
	

	
	