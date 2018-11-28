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

using namespace std;

int main() {
	int t,n,i,val,j,temp;
	int a[1000],s[1000];
	cin>>t;
	j=1;
	while(t--)
	{
		val=0;
		temp=0;
		scanf("%d",&n);
	    for(i=0;i<n+1;i++)
	    {
		    scanf("%1d",&a[i]);
	    }
	    for(i=0;i<n+1;i++)
	    {
            s[i]=i;
            if(a[i]!=0 && i==0)
            {
            	temp=temp+a[i];
            }
            if(a[i]!=0 && s[i]>temp)
            {
                 val=val+(s[i]-temp);
                 temp=temp+val;  
            }
            if(i!=0)
              temp=temp+a[i];
	    } 
	    cout<<"Case #"<<j<<": "<<val<<endl;
	    j++;
	}
	return 0;
}
