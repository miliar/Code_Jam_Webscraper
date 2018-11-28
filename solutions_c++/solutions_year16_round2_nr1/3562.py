#include<iostream>
#include<vector>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cstring>
using namespace std;

char dig[10][6];
int ldig[10];
void init()
{
	strcpy(dig[0],"ZERO");
	strcpy(dig[1],"ONE");
	strcpy(dig[2],"TWO");
	strcpy(dig[3],"THREE");
	strcpy(dig[4],"FOUR");
	strcpy(dig[5],"FIVE");
	strcpy(dig[6],"SIX");
	strcpy(dig[7],"SEVEN");
	strcpy(dig[8],"EIGHT");
	strcpy(dig[9],"NINE");
	for(int i=0;i<10;i++)
	{
		ldig[i]=strlen(dig[i]);
	}
}

int sum=0;

bool DFS(int *ptele,int &count,int* nums)
{
	int pre=0;
	if(count>0)
	{
		pre=ptele[count-1];
	}
	for(int i=pre;i<10;i++)
	{
		int j=0;
		for(;j<ldig[i];j++)
		{
			if(nums[dig[i][j]-'A']<=0)
				break;
		}
		if(j==ldig[i])
		{
			for(int j=0;j<ldig[i];j++)
				nums[dig[i][j]-'A']--;
			sum-=ldig[i];
			ptele[count++]=i;
			if(sum==0)
			{
				return true;
			}
			else if(sum>=2)
			{
				bool flag=DFS(ptele,count,nums);
				if(flag)
					return true;
			}
			count--;
			sum+=ldig[i];
			for(int j=0;j<ldig[i];j++)
				nums[dig[i][j]-'A']++;
		}
	}
	return false;
}


int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int T;
	fin>>T;
	init();
	for(int t=1;t<=T;t++)
	{
		char p[2001];
		fin>>p;
		int l=strlen(p);
		//sort(p,p+l);
		sum=l;
		int num[26];
		memset(num,0,sizeof(num));
		int tele[700];
		int count=0;
		for(int i=0;i<l;i++)
		{
			num[p[i]-'A']++;
		}

		DFS(tele,count,num);
		fout<<"Case #"<<t<<": ";
		for(int i=0;i<count;i++)
			fout<<tele[i];
		fout<<endl;

	}

	fout.close();
	fin.close();
	return 0;
}