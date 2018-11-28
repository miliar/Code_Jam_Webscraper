#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <string.h>
#include <utility>
#include <time.h>
#include <math.h>
#include <cmath>
#include <queue>
#include <set>
//freopen("input.txt", "r", stdin);
//freopen("out.txt", "w", stdout);

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef unsigned long long ullong; 
typedef long long llong;
int maxi = 0;
//int xa[] = {1,1,0,-1,-1,-1, 0, 1};
//int ya[] = {0,1,1, 1, 0,-1,-1,-1};
VI figther;
VI effort;
int xa[] = {1,0,-1, 0};
int ya[] = {0,1, 0,-1,};

VI arr;
int main()
{
    //ios_base::sync_with_stdio(false);
 
    //freopen("input.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    freopen("B-small-attempt0.IN", "r", stdin);
    freopen("B-small-attempt0.txt", "w", stdout);

    int t;
    cin >> t;
    for (int T = 1; T <= t; ++T)
     {
     	int A, B, K;
     	arr.clear();
     	cin >> A >> B >> K;
        int cont = 0;
     	for (int i = 0; i < A; ++i)
     	{
     		for (int j = 0; j < B; ++j)
     		{
     			if( (i&j) < K)cont++;
     		}
     	}


     	cout <<"Case #"<<T<<": "<<cont<<endl; 
     } 
    return 0;
}