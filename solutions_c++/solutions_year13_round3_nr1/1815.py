//============================================================================
// Name        : p1.cpp
// Author      : Mostafa Shokrof
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

bool vowel(char c)
{
	if(c=='a'||c=='u'||c=='o'||c=='i'||c=='e')
		return true;
	return false;
}
int main() {
	int ntestcases;
	cin>>ntestcases;
	for(int t=1;t<=ntestcases;t++)
	{
		string s;
		int n;
		cin>>s>>n;
		int nvalue=0;
		for(int i=0;i<s.length();i++)
		{
			for(int j=i;j<s.length();j++)
			{
				int cons=0;
				for(int k=i;k<=j;k++)
				{

					if(!vowel(s[k]))
						cons++;
					else{
						cons=0;
					}
					if(cons>=n){
						nvalue++;
						break;
					}
				}


			}
		}
		printf("Case #%d: %d\n",t,nvalue);
	}
	return 0;
}
