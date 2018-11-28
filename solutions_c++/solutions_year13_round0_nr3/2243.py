#include<iostream>
#include<stdio.h>
#include<cstring>
#include<vector>
#define MAX 10000000
using namespace std;
vector<long long int>store;
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("c.txt","w",stdout);
	int t,cases;
	long long int i,j,index,sq,num,a,b;
	store.clear();
	for(i=1;i<=MAX;i++)
	{
		sq=i;
		num=0;
		while(sq>0)
		{
			num*=10;
			num+=sq%10;
			sq/=10;
		}
		if(num!=i)
			continue;
		sq=i*i;
		num=0;
		while(sq>0)
		{
			num*=10;
			num+=sq%10;
			sq/=10;
		}
		if(num==i*i)
			store.push_back(num);
	}
	/*
	str[499]='1';
	str[500]='0';
	str[501]='1';
	str[502]='\0';
	tmpStr=str+499;
	store.push_back(tmpStr);
	check=true;
	while(true)
	{
		index=0;
		str[index+500]++;
		while(str[index+500]>'2')
		{
			str[index+500]='0';
			str[500-index]='0';
			index++;
			if(str[index]=='\0')
			{
				str[500+index]='1';
				str[500-index]='1';
				str[index+501]='\0';
				break;
			}
			else
			{
				str[index+500]++;
				str[500-index]++;
			}
		}
		tmpStr=str+500-index;
		cout<<tmpStr<<endl;
		store.push_back(tmpStr);
		if(index>60)
			break;
		
	}
	*/
	
	cin>>t;
	for(cases=1;cases<=t;cases++)
	{
		cin>>a>>b;
		for(i=0;i!=store.size();i++)
			if(store[i]>=a)
				break;
		for(j=0;j!=store.size();j++)
			if(store[j]>=b)
				break;
		if(j!=store.size())
		{
			if(store[j] > b)
				j--;
		}
		else
			j--;
		printf("Case #%d: %d\n", cases, j-i+1);
	}
	
	return 0;
}