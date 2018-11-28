#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int t2=0;
//	freopen("out.txt","w",stdout);
	while(t--){
		t2++;
		int arr[5][5];
		int n;
		cin>>n;
		for(int i=1;i<=4;i++)
		 for(int j=1;j<=4;j++)
		  cin>>arr[i][j];
		 int a[5];
		 for(int i=1;i<=4;i++)
		  a[i] = arr[n][i];
		 int m ;
		 cin>>m;
		 int ind=0;
		 int countt=0;
		 for(int i=1;i<=4;i++)
		 for(int j=1;j<=4;j++)
		  cin>>arr[i][j];
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{								
				if(a[i] == arr[m][j])
				{
					 countt++;
					ind = i;
				}
			}
		}
		if(countt==1)
		 cout<<"Case #"<<t2<<":"<<" "<<a[ind]<<endl;
		else if(countt >1)
		 cout<<"Case #"<<t2<<":"<<" "<<"Bad magician!\n";
		else
		 cout<<"Case #"<<t2<<":"<<" "<<"Volunteer cheated!\n";
	}
}
