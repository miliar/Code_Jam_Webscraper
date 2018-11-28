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
    
	int tc;
	cin>>tc;
	for(int k=1;k<=tc;k++)
	{
		double x,f,c,count,m;
		m=2;
	count =0;
	cin>>c>>f>>x;
	cout<<"Case #"<<k<<": ";
	if(x<=c)
		cout<<fixed<<setprecision(7)<<x/2<<endl;
	else 
	{
		while(true)
		{
			if((x/m)<=((c/m)+(x/(m+f))))
				break;
			count+=c/m;
			m+=f;
		}
		cout<<fixed<<setprecision(7)<<count+(x/m)<<endl;
	}
	
	}
	return 0;
}
