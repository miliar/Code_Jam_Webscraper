#include<iostream>
#include<cstring>
#include<fstream>
#include<cmath>
using namespace std;

int caseNum;
long long low,high;
long long c;

int isFair(long long);
int isSquare(long long);
int main()
{
	long long i,j;
	
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	cin>>caseNum;
	for(i=1;i<=caseNum;i++)
	{
		c=0;
		cin>>low>>high;
		for(j=low;j<=high;j++)
		{
			if(isFair(j))
			{
				if(isSquare(j))
				{
					long long temp=pow(j,0.5);
					if(isFair(temp))
						c++;
				//	cout<<j<<endl;
				}
			}
		}
		cout<<"Case #"<<i<<":"<<" "<<c<<endl;
	}
	
	return 0;
}
int isFair(long long num)
{
	char temp[150];
	int t;
	int i=0,j;
	while(num)
	{
		t=num%10;
		temp[i++]=t+'0';
		num=num/10;
	}
	temp[i]=0;
	i=0;
	j=strlen(temp)-1;
	//cout<<temp<<endl;
	while(i<j)
	{
		if(temp[i]==temp[j])
		{
			i++;
			j--;
		}
		else
		{
			break;
		}
	}
	//cout<<i<<" "<<j<<endl;
	if(i>=j)
		return 1;
	return 0;
}

int isSquare(long long num)
{
	double res;
	long long res1;
	res=pow(num,0.5);
	res1=res;
	if(res1==res)
		return 1;
	return 0;
}