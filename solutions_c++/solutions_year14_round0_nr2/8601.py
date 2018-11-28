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
typedef vector<int> VD;
typedef vector<VD> VVD;
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
 


int arr[17];

int main()
{
    //ios_base::sync_with_stdio(false);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    

    int t;
    cin >> t;
    int T = 1;
    while(t--)
    {
      double C, F , X;
      double rate = 2;
      double times = 0;
      double totalcokies;

      cin >> C >> F >> X;

      int g = 4;
      while(true)
      {



      	double time1 = X/rate;

      	double time2 = (C/rate) + (X/(rate+F));

        if(time1 < time2)
        {
               times+=time1;
               break;
        }
        else
        {
        	//cout << (C/rate) << endl;
        	times+=(C/rate);
        	rate+=F;

        }

      }
      //cout << times <<endl;
      printf("Case #%d: %.7lf\n", T ,times);
      T++;
    }

    
    return 0;
    
}
 