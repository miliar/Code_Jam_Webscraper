#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<vector>
#include<string>
#include<cmath>
#include<ctime>
#include<set>
#include<map>
 
using namespace std;

int T;
double C, F, X, m, u, r;
 
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout); 
    cin >> T;
    for (int f = 0; f < T; f++)
    {
    	m = 1e18;
    	cin >> C >> F >> X;
    	u = 2;
    	r = 0;
    	for (int i = 0; i < 2000000; i++)
    	{
    		if (r + X / u < m)
    		{
    			m = r + X / u;
       	    }
       	    r += C / u;
       	    u += F;
       	}
    	cout << "Case #" << f + 1 << ": ";
    	printf("%.8lf", m);
    	cout << endl;
    }

    return 0;
}