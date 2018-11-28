#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	
	int t,n,g=1;
	cin>>t;
	while(g<=t)
	{
		cin>>n;
		int p[n];
		int maxi=-1;
		for(int i=0;i<n;i++)
		{
			cin>>p[i];
			maxi=max(maxi,p[i]);
		}
		vector<vector<int> > h(maxi+1);
		for(int i=0;i<n;i++)
		{
			h[p[i]].push_back(i);
		}
		cout<<"Case #"<<g<<": ";
		for(int j=maxi;j>0;j--)
		{
			
			char c,c2;
			int k,k2;
			while(h[j].size()>0)
			{
				int r=h[j].size();
				if(r%2)
				{
					k=h[j][r-1];
					c=k+'A';
					if(j==1)
					{
					cout<<c<<" ";
					h[j-1].push_back(k);
					}
					else
					{
						cout<<c<<c<<" ";
						h[j-2].push_back(k);
					}
					h[j].resize(r-1);
				}
				else
				{
				     k=h[j][r-1],k2=h[j][r-2];
					 c=k+'A';
					 c2=k2+'A';
					 cout<<c<<c2<<" ";
					 h[j-1].push_back(k);
					 h[j-1].push_back(k2);
					 h[j].resize(r-2);
				}
			}
		}
			g++;
			cout<<"\n";
	}
	return 0;
}