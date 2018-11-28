#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <assert.h>
#include <queue>
#include <string>
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pp pop_back
#define ll long long int
#define pii pair<int,int>

using namespace std ;

int main()
{
    ios_base::sync_with_stdio(false) ;

    cin.tie(0) ;

    freopen("GCJ-2-A.txt" , "w" , stdout) ;

    int T , run = 0 ;

    cin >> T ;

    while(T--)
    {
    	string inp ;

    	cin >> inp ;

    	int len = inp.length() , countx = 0 ;

    	int j = len - 1 , i = 0 , k , flag = 0 ;

    	for(k = j ; k >= 0 ; k--)
    	{
    		if(inp[k] == '+')
    			continue ;

    		else
    		{
    			inp[k] = '+' ;

    			countx++ ;

    			for(i = k - 1 ; i >= 0 ; i--)
    			{
    				if(inp[i] == '-')
    				{
    					inp[i] = '+' ;
    					continue ;
    				}

    				else
    					break ;
    			}

    			k = i ;

    			for(int m = k ; m >= 0 ; m--)
    				inp[m] == '+' ? inp[m] = '-' : inp[m] = '+' ;

    			k++ ;
    		}
    	}

    	cout << "Case #" << ++run << ": " << countx << '\n' ;
    }

    return 0 ;
}


