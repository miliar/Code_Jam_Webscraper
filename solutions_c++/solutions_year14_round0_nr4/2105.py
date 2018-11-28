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
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 

 
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int tc,t;
	cin>>tc;
	for(int k=1;k<=tc;k++)
	{
		cin>>t;
		double arr[10001],arr1[10001];
		for(int i=0;i<t;i++)
			cin>>arr[i];
		for(int i=0;i<t;i++)
			cin>>arr1[i];
		sort(arr,arr+t);
		sort(arr1,arr1+t);
		int c,c1;
		c=c1=0;
		for(int i=t-1,j=t-1;j>=0,i>=0;i--,j--)
		{
			if(j<0||i<0)
				break;
			if(arr[i]>arr1[j])
				c++;
			else 
				i++;
		}
		for(int i=t-1,j=t-1;j>=0,i>=0;i--,j--)
		{
			if(j<0||i<0)
				break;
			if(arr[i]<arr1[j])
				c1++;
			else 
				j++;
		}
		cout<<"Case #"<<k<<": "<<c<<" "<<t-c1<<endl;
	}
	return 0;
}
