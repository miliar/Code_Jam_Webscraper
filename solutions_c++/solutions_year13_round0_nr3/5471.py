#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <cmath>
#include <fstream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;
bool is (long long n)
{
	if (n <10)
	return true ;
	stringstream s;
	s<<n ; 
	string ss;
	s>>ss;
	bool isP=true;
	for (int i =0 , j = ss.size()-1 ; i <j ; i++ , j--)
	{
		if ( ss[i]!=ss[j])
		isP=false;
	}
	return isP;
	
}
int main()
{
	freopen("C-small-attempt0.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
    freopen("C-small-attempt0.out", "wt", stdout); // same for out.txt
	int T; 
	cin>>T;
	for (int i =0 ; i < T ; i++)
	{
		int m ,n ; 
		cin >>m>>n ;
		int c=0;
		for (int k = m ; k <=n ; k++)
		{
			
			if (is(k))
			{
			double sq = sqrt(k)	;
			
			
			int s2 = (int )sqrt(k);
			double d= sq-s2;
			if (d==0)
			{
			if (is(sq))
			c++;
	     	}	
			}
			
		}
		
		cout<<"Case #"<<i+1<<": "<<c<<endl;
		
	}
	

    return 0;
}
