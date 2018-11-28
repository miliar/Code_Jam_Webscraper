//BIG-OH
//prob-
//Algo-
//complexity-
#include<cstdio>
#include<iostream>
#include<cstring>
#include<sstream>
#include<stdlib.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<iomanip>
#include<ctype.h>
#include<complex>
#include<utility>
#include<functional>
#include<bitset>
#include<numeric>
#include<cassert>
#include<climits>
 
using namespace std;
#define ll long long 
#define gc getchar_unlocked
#define mod 1000000009
#define pq priority_queue
#define vi vector<int>
#define eps 1e-9
#define inf (1 << 28)
#define  MX 1111111
int main()
{
  int test;
  cin>>test;
  for(int i=0;i<test;++i)
  {
	int a=0,b=0,tmp;    
	char str[1001];
	cin>>tmp;
	cin>>str;	    
	for(int j=0;j<=tmp;++j)
       {
	        
	        if(a>=j) a+=str[j]-'0';
	        else
                {
	            
	            ++b;
	            ++a;
	            a+=str[j]-'0';
	            
	        }
	    }
	    
	    cout<<"Case #"<<i+1<<": "<<b<<endl;
	    
	}

	return 0;
}
