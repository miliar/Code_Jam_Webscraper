#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int arr[26][2]={0};
		vector < vector<int> > myVector(26,vector<int>(2));
		int n;
		cin>>n;
		for(int i=0;i<n;i++) cin>>myVector[i][0],myVector[i][1]=i+1;
		cout<<"Case #"<<k<<": ";
		while(1)
		{
			std::sort(myVector.begin(), myVector.end(), [](const std::vector< int >& a, const std::vector< int >& b){ return a[0] > b[0]; } );
			//for(int i=0;i<n;i++) cout<<myVector[i][0]<<" "<<myVector[i][1]<<endl;
			if((myVector[0][0]>myVector[1][0] && myVector[0][0]!=0) || (myVector[0][0]==1 && myVector[0][0]==myVector[1][0] && n>2 && myVector[2][0]==1))
			{
				myVector[0][0]--;
				char c=myVector[0][1]-1+'A';
				cout<<c<<" ";
			}
			else if(myVector[0][0]==myVector[1][0] && myVector[0][0]!=0 && myVector[1][0]!=0)
			{
				myVector[0][0]--;
				myVector[1][0]--;
				char c=myVector[0][1]-1+'A';
				char d=myVector[1][1]-1+'A';
				cout<<c<<d<<" ";
			}
			else
			{
				cout<<endl;
				break;
			}
		}
	}
	return 0;
}
