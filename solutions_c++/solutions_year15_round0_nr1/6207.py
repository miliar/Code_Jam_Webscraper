# include<iostream>
# include<conio.h>

using namespace std;

int main()
{
	int T,S;
	char str[1000];
	int a[1000];
	int i,j,no;
	int ps;//People Stood Up
	int ans[100];
	cin>>T;
	for(i=0;i<T;i++)
	{
		ans[i]=ps=0;
		cin>>S;
		cin>>str;
		for(j=0;j<S+1;j++)
		{
			no=str[j]-'0';
			if(j==0)
				ps=no;
			else if(no!=0)
			{
				if(ps<j)
				{
					//ans[i]++;
					//ps++;
					ans[i]+=j-ps;
					ps=j+no;
				}
				else
					ps+=no;
			}
		}
	}
	for(i=0;i<T;i++)
		cout<<"\nCase #"<<i+1<<": "<<ans[i];

	getch();
}