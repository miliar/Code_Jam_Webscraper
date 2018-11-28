#include<iostream>
#include<cstring>
#include<cmath>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

bool isPalin(char str[])
{
	int len = strlen(str);
	if(len < 2)
	return true;
	for(int i = 0; i < len/2; i++)
	{
		if(str[i] != str[len - i - 1])
		return false;
	}
	return true;
}

void increment(char str[])
{
	int len = strlen(str);
	
	bool allNines = true;
	for(int i = 0; i < len; i++)
	{
		if(str[i] != '9')
		allNines = false;
	}
	if(allNines)
	{
		str[0] = '1';
		for(int i = 1; i <= len; i++)
		str[i] = '0';
		str[len + 1] = '\0';
		return;
	}
	
	for(int i = len - 1; i >= 0; i--)
	{
		if(str[i] != '9')
		{
			str[i]++;
			break;	
		}
		else
		{
			str[i] = '0';
		}
	}
}

int main(void)
{
	freopen("C:/Downloads/C-large-1.in", "r", stdin);
	freopen("C:/Downloads/GCJ-QR-C-Large-Out.txt", "w+", stdout);
	int T;
	cin>>T;
	int n = 1;
	long long int A, B, F[39] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
	while(T--)
	{
		cin>>A>>B;
		int num = 0;
		for(int i = 0; i < 39; i++)
		{
			if(F[i] >= A && F[i] <= B)
			num++;
		}
		cout<<"Case #"<<n++<<": "<<num<<endl;
	}
}
