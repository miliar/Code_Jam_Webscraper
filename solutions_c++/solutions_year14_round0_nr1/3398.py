#include <iostream>

using namespace std;


int main() {
	int t,ans1,ans2,a[5][5],b[5][5],c[5],d[5],k,count,l,i,j,ans,w;
	cin>>t;
	for(w=1;w<=t;w++)
	{

		cin>>ans1;
		k=1;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>a[i][j];
				if(i==ans1)
				{
					c[k]=a[i][j];
					k++;
				}
			}
		}
		cin>>ans2;
		l=1;
			for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>b[i][j];
				if(i==ans2)
				{
					d[l]=b[i][j];
					l++;
				}
			}
		}

		
		count=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(c[i]==d[j])
				{
					count++;
					ans=d[j];
				}
			}
		}
		if(count==1)
		cout<<"Case #"<<w<<": "<<ans<<endl;
		else if(count>1)
		cout<<"Case #"<<w<<": "<<"Bad magician!"<<endl;
		else
		cout<<"Case #"<<w<<":"<<" "<<"Volunteer cheated!"<<endl;


	}
	return 0;
}
