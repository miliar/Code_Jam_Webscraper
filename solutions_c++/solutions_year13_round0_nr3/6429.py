#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include<sstream>
using namespace std;

int main()
{
unsigned long long tt,t,i,index,a,b,cnt;
string str1,str2;
std::stringstream strm;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
cin>>tt;
for(t=1;t<=tt;t++)
{
	cin>>a;
	cin>>b;
	cnt=0;
	for(i=a;i<=b;i++)
	{
	
	strm<<std::dec;
	strm<<i;
	str1=strm.str();
	str2=str1;
	reverse(str2.begin(),str2.end());
	//cout<<"\n str1 = "<<str1<<"  str2 ="<<str2<<"\n";
	if(str2==str1)
	{

		index=round(sqrt(i));
		if(i==((index)*(index)))
		{
			//cout<<"\n "<<i<<" found"<<"\n"<<"index = "<<index<<"\n";
			str1.clear();
			str2.clear();
			strm.str(std::string());
        		strm.clear();
			strm<<std::dec;
			strm<<index;
			str1=strm.str();
			str2=str1;
			reverse(str2.begin(),str2.end());
			if(str2==str1)
			{
				
			//	cout<<"\n str1 = "<<str1<<"  str2 ="<<str2<<"\n";
				cnt++;
			}
		}
	}

		str1.clear();
		str2.clear();
		strm.str(std::string());
		strm.clear();
		
	}
	cout<<"Case #"<<t<<": "<<cnt<<"\n";
}

return 0;
}
