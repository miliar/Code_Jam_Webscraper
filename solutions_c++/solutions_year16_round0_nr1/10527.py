#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;
int c[10];
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	    
	    long long res;
	    cin>>res;
	    cout<<"Case #"<<i+1<<": ";
	    if(res==0)
	    {
	        cout<<"INSOMNIA"<<endl;
	        continue;
	    }
	    bool isOK=true;
	    for(int i=0;i<10;i++)
	     c[i]=0;
	    for(long long i=1;i<1000;i++)
	    {
	      long long temp=i*res;
	     // cout<<temp<<endl;
	      isOK=true;
	      while(temp>0)
	      {
	        c[temp%10]++;
	        temp/=10;
	        
	      }
	     
	      for(int i=0;i<10;i++)
	      if(!c[i])
	         isOK=false;
	      if(isOK)
	      {
	          cout<<i*res<<endl;
	          break;
	      }
	       
	    }
	    if(!isOK)
	    {
	        cout<<"INSOMNIA"<<endl;
	    }
	}
}