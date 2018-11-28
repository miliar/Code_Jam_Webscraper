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
#define RR 50
#define CC 50
char str[RR][CC];
long long Solve(long long x,long long y,long long z)
{
	long long temp;
	long long num=0;
	for(long long i=0;i<x;i++){
		for(long long j=0;j<y;j++){
			temp=i&j;
			if(temp<z)
				num++;
		}
	}
	return num;
}
#define TRY
#define SMALL
//#define LARGE
int main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
	int Numcase;
	cin>>Numcase;
	long long a,b,c;
	for(int test=1;test<=Numcase;test++)
	{
		cout<<"Case #"<<test<<": ";
		cin>>a>>b>>c;
		cout<<Solve(a,b,c)<<endl;
	}
}