#include<iostream>
using namespace std;
int main()
{
	int test,x,y,arr1[4][4],arr2[4][4],i,j,ans1[4],ans2[4],flag=0,flag1=0,a=1,ans;
	cin>>test;
	while(test--)
	{
		cin>>x;
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
		        cin>>arr1[i][j];
		//cout<<"ans1 :\n";
		for(i=0;i<4;i++)
		{
			ans1[i]=arr1[x-1][i];
			//cout<<ans1[i]<<endl;
		}
		cin>>y;
		//cout<<"ans2 :\n";
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
		        cin>>arr2[i][j];
		flag=0;
		flag1=0;
		for(i=0;i<4;i++)
		{
			ans2[i]=arr2[y-1][i];
			//cout<<ans2[i]<<endl;
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if((ans1[i]==ans2[j])&(flag==0))
				{
				   flag=1;
				   ans=ans1[i];
				   //cout<<"ans :"<<ans<<endl;
				   //cout<<"i :"<<i<<"  j :"<<j<<endl;
				}
				else if((ans1[i]==ans2[j])&(flag==1)&(flag1==0))
				{
				    flag1=1;
				    //cout<<"2 ans :"<<ans1[i]<<endl;
				    //cout<<"i :"<<i<<"  j :"<<j<<endl;
				    break;
				}
			}
			if(flag1==1)
			    break;
		}
		if(flag1==1)
		    cout<<"Case #"<<a<<": Bad magician!\n";
		else if(flag==0)
		    cout<<"Case #"<<a<<": Volunteer cheated!\n";
		else
		    cout<<"Case #"<<a<<": "<<ans<<"\n";
		a++;
	}
	return 0;
}
