#include<iostream>

using namespace std ;

void check(int a[] ,int ans[])
{
	if(a[26]!=0)//0
	{
		ans[0]++;
		a[26]--;
		a[5]--;
		a[18]--;
		a[15]--;
		check(a,ans);
	}
	
	else if (a[21]!=0)//4
	{
		ans[4]++;
		a[6]--;
		a[15]--;
		a[21]--;
		a[18]--;
		check(a,ans);
	}
	else if (a[24]!=0)//6
	{
		ans[6]++;
		a[19]--;
		a[9]--;
		a[24]--;
		check(a,ans);
	}
	else if (a[23]!=0)//2
	{
		ans[2]++;
		a[20]--;
		a[23]--;
		a[15]--;
		check(a,ans);
	}
	else if (a[7]!=0)//8
	{
		ans[8]++;
		a[5]--;
		a[9]--;
		a[7]--;
		a[8]--;
		a[20]--;
		check(a,ans);
	}
	else if (a[15]!=0)//1
	{
		ans[1]++;
		a[15]--;
		a[14]--;
		a[5]--;
		check(a,ans);
	}
	else if(a[19]!=0)//7
	{
		ans[7]++;
		a[19]--;
		a[5]-=2;
		a[22]--;
		a[14]--;
		check(a,ans);
	}
	else if (a[22]!=0)//5
	{
		ans[5]++;
		a[22]--;
		a[6]--;
		a[9]--;
		a[5]--;
		check(a,ans);
	}
	else if (a[9]!=0)//9
	{
		ans[9]++;
		a[14]-=2;
		a[9]--;
		a[5]--;
		check(a,ans);
	}
	else if(a[18]!=0)//3
	{
		ans[3]++;
		a[20]--;
		a[8]--;
		a[18]--;
		a[5]-=2;
		check(a,ans);
	}
	
	return ;
}

int main()
{
	int t;
	char x[102];
	int ans[10];
	int a[27] , i , k=1;
	
	cin>>t;
	while(t--)
	{
		for(i=0;i<27;i++)
		{
			a[i] = 0;
			ans[i] = 0;
		}
		
		cin>>x;
		for(i=0;x[i];i++)
			a[(int)x[i] - 64]++;
	
		check(a,ans);
		cout<<"Case #"<<k++<<": ";
	
		
		for(i=0;i<10;i++)
		{
			for(int j=0;j<ans[i];j++)
			{
				cout<<i;
					}		
		}		
		
		
		cout<<endl;
	}		
}
