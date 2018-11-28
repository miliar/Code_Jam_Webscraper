#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <functional>
#include <list>
#include <string>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long ll;

int main()
{
	string s;
	ifstream in;
	ofstream out;
	in.open("B.in");
	out.open("B.out");
	
	int t;
	in>> t;
	
	for(int i=1;i<=t;i++)
	{
		int a[2501],n,temp;
		memset(a,0,sizeof(a));
		in>>n;
		for(int j=1;j<=2*n-1;j++)
		{
			for(int k=1;k<=n;k++)
			{
			
			
				in>>temp;
				a[temp]++;
			
			}
		}
		int count =0;
		out<<"Case #"<<i<<":";
		for(int j=1;j<=2500;j++)
		{
			if(a[j]%2!=0)
			{
				out<<" "<<j;
				count++;
			}
		}
		out<<"\n";
		
		
	}
	
	
	return 1;
}
