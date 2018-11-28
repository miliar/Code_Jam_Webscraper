#include<iostream>
#include<cmath>
#define ull unsigned long long
using namespace std;

ull deletes[11];

bool badword(ull structur,int i)
{
	ull j;
	for (j=2; j<=sqrt(structur+0.); j++)
	{
		if (structur%j==0)
		{
			deletes[i]=j;
			return false;
		}
	}
	return true;
}

bool correct(ull matchs[],ull num1,ull i)   
{
	ull structur=0,P=1,j;
	for (j=0; j<num1; j++)
	{
		structur+=matchs[num1-1-j]*P;
		P*=i;
	}
	return (!badword(structur,i));    
}

bool newfuncruss(ull matchs[],ull num1)
{
	for (int i=2; i<=10; i++)
	{
		if (!correct(matchs,num1,i))         
		{
			return false;
		}
	}
	return true;
}

void func(ull vars2,ull num1,ull matchs[])
{
	int j=num1-2;
	for (int i=1; i<=num1-2; i++)
	{
		matchs[i]=0;
	}
	while (vars2!=0)
	{
		matchs[j]=vars2%2;
		vars2=int(vars2/2);
		j--;
	}
}

int main()
{
	ull matchs[32],jawa,num1,testCases,i,var1,bigVar=1,vars2;
	cin>>testCases;
	for (i=1; i<=testCases; i++)
	{
		cin>>num1>>jawa;
		var1=0;
		cout<<"Case #"<<i<<":"<<endl;
		matchs[0]=1;
		matchs[num1-1]=1;
		for (vars2=1; vars2<=num1-2; vars2++)          
		{
			bigVar*=2;
		}
		for (vars2=0; vars2<=bigVar && var1!=jawa; vars2++)
		{
			func(vars2,num1,matchs);
			if (newfuncruss(matchs,num1))
			{
				for (int query=0; query<num1; query++)
				{
					cout<<matchs[query];
				}
				cout<<" ";
				for (int query=2; query<=10; query++)
				{
					cout<<deletes[query]<<" ";
				}
				cout<<endl;
				var1++;
			}
		}
	}
	return 0;
}
