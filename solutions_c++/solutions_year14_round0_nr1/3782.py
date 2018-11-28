#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<fstream>
using namespace std;
#define getchar_unlocked getchar
#define ll long long int
inline long long int in()
{
   long long int n=0;
   long long int ch=getchar_unlocked();
   long long int sign=1;
   while( ch < '0' || ch > '9' )
   {
   	if(ch=='-')sign=-1; ch=getchar_unlocked();
	   }
 
   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
   return n*sign;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Problem_a_output.txt","w",stdout);
	ll t;
	t=in();
	for(int x=1;x<=t;x++)
	{
		ll first,arr1[4][4],second,arr2[4][4],ct=0,ans=0;
		bool a1[17];
		memset(a1,0,sizeof(a1));
		first=in();
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				arr1[i][j]=in();
				if(i+1==first)
				a1[arr1[i][j]]=1;
			}
		}
		second=in();
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				arr2[i][j]=in();
				if(i+1==second)
				{
					if(a1[arr2[i][j]]==1)
					{
						ans=arr2[i][j];
						ct++;
					}
						
				}
			}
		}
		if(ct==0)
		cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<"\n";
		else if(ct==1)
		cout<<"Case #"<<x<<": "<<ans<<"\n";
		else if(ct>1)
		cout<<"Case #"<<x<<": "<<"Bad magician!"<<"\n";
	}
	
}

