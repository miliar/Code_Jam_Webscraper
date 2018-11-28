#include<iostream>
#include<stdio.h>
using namespace std;
int main()

{
	freopen("C:\\users\\mobasser\\Google Drive\\uva\\in.txt","rt",stdin);
	freopen("C:\\users\\mobasser\\Google Drive\\uva\\out.txt","wt",stdout);
	int n[7];
	int test,smax,people=0,i,j,need=0,ans=0;
	cin>>test;
	for(i=0;i<test;i++)
	{
		cin>>smax;
		for(j=0;j<=smax;j++)
		scanf("%1d",&n[j]);

		for(int k=0;k<=smax;k++)
		{
			if(n[0]==0&& k==0){
				ans++;
				people++;
			}


			if(people<k){

				need=k-people;

				people=people+need;
				ans=ans+need;


			}
			people=people+n[k];

		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		need=0,people=0,ans=0;

	}

}
