#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <fstream>
#include <string>
#include <cmath>
#include <queue>
 
using namespace std;
 
int main()
{
	//freopen("INPUT.TXT","r",stdin); freopen("OUTPUT.TXT","w",stdout);
	int t;
	double c, f, x;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>c>>f>>x;
		int k = 0;
		double S = 0, A = x/2, best = A;
		bool go = true;
		int cnt = 10; //for shure
		while (cnt)
		{
			double Aprev = A;
			S = S + 1.0/((k++)*f+2);
			A = c * S + x / (k*f + 2);
			best = min(A, best);
			if(go)
				go = A < Aprev;
			else
				cnt--;
		}
		cout<<"Case #"<<i<<": ";
		printf("%.8f\n", best);
		
	}
	
}