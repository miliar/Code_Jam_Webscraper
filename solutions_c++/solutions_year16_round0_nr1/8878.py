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
#include <typeinfo>
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

    freopen("GCJ-1-A.txt" , "w" , stdout) ;

    ll T , inp , var , run = 0 ;

    cin >> T ;

    while(T--)
    {
    	cin >> inp ;

    	var = inp ;

    	if(inp == 0)
    	{
    		cout <<"Case #" << ++run << ": " << "INSOMNIA" << '\n' ;
    		continue ;
    	}

    	ll freq[10] ;

    	for(int i = 0 ; i < 10 ; i++) freq[i] = 0 ;

    	string s2 ;

    	int k = 2 ;

    	while(1) {

    		int flag = 0 ;

	    	s2 = to_string(var) ;

	    	for(int i = 0 ; i < s2.length() ; i++)
	    		freq[s2[i] - '0']++ ;

	    	for(int i = 0 ; i < 10 ; i++)
	    	{
	    		if(freq[i] == 0)
	    			{
	    				flag = 1 ;
	    				break ;
	    			}
	    	}

	    	//string::size_type sz ;

	    	if(flag)
	    	{
	    		//inp = stoi(s2 , &sz) ;
	    		var = inp * k ;
	    		k++ ;
	    	}

	    	else
	    	{
	    		cout <<"Case #" << ++run << ": " << var << '\n' ;
	    		break ;
	    	}
    	}
    	
    }

    return 0 ;
}


