#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	for(int x=1;x<=t;x++)
	{
		int n,m;
		int a[4][4],b[4][4];
		cin>>n;
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
				
		cin>>m;
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
				
		vector<int> s;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[n-1][i]==b[m-1][j])
					s.push_back(a[n-1][i]);
			}
		}
		
		cout<<"Case #"<<x<<':'<<" ";
		
		if(s.size()==1)
			cout<<s[0];
		else if(s.size()==0)
			cout<<"Volunteer cheated!";
		else
			cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}
