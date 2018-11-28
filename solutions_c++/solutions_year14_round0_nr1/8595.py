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
 
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.txt", "w", stdout);

    int t;
    cin >> t;
    int T = 0;
    while(T<t)
    {  
    	int a;
    	int b;
    	int sq1[4][4];
        int sq2[4][4];
        int c;
        memset(arr, 0 , sizeof arr );
        cin >> a;
        for (int i = 0; i < 4; ++i)
        {
        	for (int j = 0; j < 4; ++j)
        	{
        		cin >> c;
        		if(i==a-1) arr[c]++;
        	}
        }


        cin >> b;

        for (int i = 0; i < 4; ++i)
        {
        	for (int j = 0; j < 4; ++j)
        	{
        		cin >> c;
        		if(i==b-1) arr[c]++;
        	}
        }
        int res = 0;
        bool complete = true;
        bool finis = false; 
        for (int i = 0; i < 17; ++i)
        {
        	//cout << arr[i] << endl;
        	if(arr[i] == 2 && complete)
        	{
        		res = i;
        		complete = false;
        	}
        	else if(arr[i] == 2 && complete == false)
        	{
              finis = true;
        	}
        }
         if(complete == true)cout << "Case #"<<T+1<<": Volunteer cheated!"<<endl;
         else if(complete == false && finis == false) cout << "Case #"<<T+1<<": "<<res<<endl;
         else if(complete == false && finis == true)cout << "Case #"<<T+1<<": Bad magician!" <<endl;
        T++;

    }


    return 0;
    
}
 