#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

#define SMALL
using namespace std;

int main()
{
	
#ifdef SMALL
	freopen("A-small-practice.in","rt",stdin);
#else
	freopen("B-large-practice.in","rt",stdin);
#endif
	freopen("out.out","wt",stdout);
	
	int N,t=1;
	cin>>N;
	cin.ignore();
	while(N--)
	{
		cout<<"Case #"<<t++<<": ";

		double C,F,X,rate=2,sec=0;

		cin>>C>>F>>X;

		while(C/rate+X/(rate+F)<X/rate)
		{
			
			sec+=C/rate;
			rate+=F;
		}

		sec+=X/rate;

		printf("%.7f",sec);
		cout<<"\n";
	}


	return 0;
}
