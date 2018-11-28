// CodeJam 2014: sudip1401
#include <iostream>
#include <vector>
using namespace std;

int a[4][4], b[4][4];
vector<int> v;

int main() {
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		int r1,r2;
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		cin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		
		r1--;
		r2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[r1][i] == b[r2][j])
					v.push_back(a[r1][i]);
		
		if(v.size() == 0)
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if(v.size() == 1)
			cout<<"Case #"<<t<<": "<<v[0]<<endl;
		else 
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
			
		v.clear();
	}
	return 0;
}
