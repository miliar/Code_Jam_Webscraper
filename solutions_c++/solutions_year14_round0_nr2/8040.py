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
#include<cstring>
using namespace std;
int main()
{
	std::cout.precision(30);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		float c,x,f;
		cin>>c>>f>>x;
		float con=2,ans;
		float p=x/con,i=0,sum=0;
		while(1)
		{
			sum=sum+c/(con+i*f);
			i=i+1.0;
			ans=sum+x/(con+i*f);
			if(ans>=p)
			break;
			p=ans;
			
		}
		//printf("Case #%d: %7f\n",test,p);
		cout<<"Case #"<<test<<": "<<p<<endl;
	}
	return 0;
}
