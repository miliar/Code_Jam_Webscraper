#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

#define assert(f) { if(!(f)) { fprintf(stderr,"Assertion failed: "); fprintf(stderr,#f); fprintf(stderr,"\n"); exit(1); } }

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

ifstream fin("input.txt");

ofstream fout("output.txt");

int output=-1;
int solve(int a,int b,int order)
{
	if(a == b )
		return order;
	if(order>40)
		return -1;
	if(a>b)
	{
		a=a-b;
		if(output==-1)
			output = order;
	}
	else if(b%2==0)
	{
		b = b/2;
	}
	else
		a*=2;
	solve(a,b,order+1);


}
int main()
{
	int test_cases;
	fin>>test_cases;
	int n=1;
	while(test_cases--)
	{
		output=-1;
		string stri;
		fin>>stri;
		int i = stri.find("/");
		int a = atoi(stri.substr(0,i).c_str());
		int b = atoi(stri.substr(i+1,stri.length()).c_str());
		int result = solve(a,b,0);
		if(result==-1)
		fout<<"Case #"<<n<<": "<<"impossible"<<endl;
		else if(output!=-1)
		fout<<"Case #"<<n<<": "<<output<<endl;
		else
		fout<<"Case #"<<n<<": "<<result<<endl;
		n++;
	}
	return 0;
}