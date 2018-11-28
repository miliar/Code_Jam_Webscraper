#include<iostream>
#include<iomanip>
#include<math.h>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int val(const char * a)
{
	if(!strncmp(a,"1",2))
		return 0;
	if(!strncmp(a,"i",2))
		return 1;
	if(!strncmp(a,"j",2))
		return 2;
	if(!strncmp(a,"k",2))
		return 3;
	if(!strncmp(a,"-1",2))
		return 4;
	if(!strncmp(a,"-i",2))
		return 5;
	if(!strncmp(a,"-j",2))
		return 6;
	if(!strncmp(a,"-k",2))
		return 7;
}

int main()
{

	string quaternion[8][8] = {{"1","i","j","k","-1","-i","-j","-k"},{"i","-1","k","-j","-i","1","-k","j"},{"j","-k","-1","i","-j","k","1","-i"},{"k","j","-i","-1","-k","-j","i","1"},{"-1","-i","-j","-k","1","i","j","k"},{"-i","1","-k","j","i","-1","k","-j"},{"-j","k","1","-i","j","-k","-1","i"},{"-k","-j","i","1","k","j","-i","-1"}};
	int T;
	int L[102],X[102];
	string pat[102],temp;
	int out[102];
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>L[i]>>X[i];
		getline(cin,temp);
		getline(cin,pat[i]);
	}
	for(int i=1; i<=T; i++)
	{
		string value = "1";
		int test = 0;
		if(L[i]*X[i]<3 || L[i] <2)
		{
			out[i]=0;
			continue;
		}
		for(int j = 0; j< X[i]; j++)
		{
			for(int k = 0; k<L[i]; k++)
			{
				temp=pat[i][k];
				value = quaternion[val(&value[0])][val(&temp[0])];
				if((!strncmp(&value[0],"i",2)) && test==0)
				{
						test++;
						value = '1';
						continue;
				}
				else if((!strncmp(&value[0],"j",2)) && test==1)
				{
						test++;
						value = '1';
						continue;
				}
				else if((!strncmp(&value[0],"k",2)) && test==2)
				{
						test++;
						value = '1';
						continue;
				}
			}
		}
		if((!strncmp(&value[0],"1",2)) && test==3)
			out[i] = 1;
		else
			out[i] = 0;
	}
	for (int i = 1; i <= T; i++)
	{
		string result=(out[i]==1)?"YES":"NO";
		cout<<"Case #"<<(i)<<": "<<result<<"\n";
	}
	return 0;
}
