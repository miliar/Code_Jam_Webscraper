#include <stdio.h>
#include <string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<string>
#include<cstdio>
#include<sstream>
#include<map>
#include<list>
#include<queue>
#include<set>
#include<numeric>
#include<functional>
#include <bitset> // compact STL for Sieve, more efficient than vector<bool>!
using namespace std;
int main() {
	int t,n,num,out,size;
	string s;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		cin>>n>>s;
		num=0;
		out=0;
		size=(int)s.size();
		for (int j = 0; j < size; j++)
		{
			if(num<j && s[j]!='0')
			{	
				out+=(j-num);
				num+=(j-num);
			}
			num+=(s[j]-'0');
		}
		printf("Case #%d: %d\n",i+1,out);
	}
	return 0;
}