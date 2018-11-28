#include<iostream>
using namespace std;
int main()
{
int t,arr[4][4],i,j,ans1,ans2,var1,var2,var3,var4,n;
cin>>t;
 for(int ii=0;ii<t;ii++)
 {
 	cin>>ans1;
 	for(i=1;i<=4;i++)
 	{
 		if(i==ans1)
 		{
 			cin>>var1>>var2>>var3>>var4;
 			}
 			else
 			{
 				for(j=1;j<=4;j++)
 				cin>>n;
 			}
 	}
 	
 	cin>>ans2;
 	int cnt=0,ele;
 	bool flag=0;
 	for(i=1;i<=4;i++)
 	{
 		if(i==ans2)
 		{
 			
 			for(j=0;j<4;j++)
 			{
 			cin>>n;
 			if(n==var1 || n==var2 ||n==var3 ||n==var4)
 			{
 			cnt++;
 			ele=n;
 			}
 			}
 		}
 		else
 		{
 			for(j=0;j<4;j++)
 			cin>>n;
 		}
 	}
 	if(cnt==1)
 	cout<<"Case #"<<ii+1<<": "<<ele<<endl;
 	if(cnt>1)
 	cout<<"Case #"<<ii+1<<": "<<"Bad magician!"<<endl;
 	if(cnt==0)
 	cout<<"Case #"<<ii+1<<": "<<"Volunteer cheated!"<<endl;
 }
 return 0;
 }

 	
