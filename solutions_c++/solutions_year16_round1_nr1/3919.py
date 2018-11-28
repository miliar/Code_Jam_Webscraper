#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		string str;
		deque<char>str1,str2;
		cin>>str;
		int x,y,i;
		x=str.size();
		str2.push_front(str[0]);
		for(i=1;i<x;i++)
		{
			deque<char>::iterator iter = str2.begin();
			y= *iter - str[i];
			if(y>0)
				str1.push_back(str[i]);
			else str2.push_front(str[i]);
		}
		printf("Case #%d: ",k);
		deque<char>::iterator iter2 = str2.begin();
		while(iter2!= str2.end())
		{
			cout<<*iter2;
			iter2++;
		}
		deque<char>::iterator iter3 = str1.begin();
		while(iter3!= str1.end())
		{
			cout<<*iter3;
			iter3++;
		}
		cout<<endl;
	}
	return 0;
}
