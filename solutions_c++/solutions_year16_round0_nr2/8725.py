/*
Input 
 5
-
-+
+-
+++
--+-	
Output 
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
*/
#include<iostream>
#include<stdio.h>
using namespace std;
char opp(char target)
{
	if(target =='+')
		return '-';
	else
		return '+';
}
int fun(string str , int lastInd, char target)
{
	if(lastInd==0)
	{
		if(str[lastInd]==target)
			return 0;
		else
			return 1;
	}
		
	int flips = 0 ;
	if(str[lastInd]==target)
	{
		flips = flips + fun(str,lastInd-1,target);
	}
	else
	{
		flips = flips + fun(str,lastInd-1,opp(target));
		flips = flips +1;
	}
	return flips;
}
int main()
{
	
	int T;
	cin>>T;
	for(int i =0;i<T;i++)
	{
		string str;
		cin>>str;
		int flips = fun(str,str.size()-1,'+');
		cout<<"Case #"<<i+1<<": "<<flips<<"\n";
	}
	
}