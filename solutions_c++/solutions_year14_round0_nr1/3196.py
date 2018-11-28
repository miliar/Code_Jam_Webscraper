# include <iostream>
# include <sstream>
# include <vector>
using namespace std;
int arr1[16][16];
int arr2[16][16];

int main()
{   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n_cases;cin>>n_cases;
	for(int x=1;x<=n_cases;x++)
	{   int first;cin>>first;
	    for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr1[i][j];
		int ops1[4];
		for(int i=0;i<4;i++)
			ops1[i]=arr1[first-1][i];
			
		int second;cin>>second;
		for(int i=0;i<4;i++)
		    for(int j=0;j<4;j++)
		        cin>>arr2[i][j];
		int ops2[4];
		for(int i=0;i<4;i++)
		    ops2[i]=arr2[second-1][i];

		vector<int>sol;
		for(int i=0;i<4;i++)
		    for(int j=0;j<4;j++)
		        if(ops1[i]==ops2[j])
		            sol.push_back(ops1[i]);
		if(sol.size()==0)
		    cout <<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl;
		if(sol.size()==1)
		    cout <<"Case #"<<x<<": "<<sol[0]<<endl;
		if(sol.size()>1)
		    cout <<"Case #"<<x<<": "<<"Bad magician!"<<endl;
	}
}
		    
		    
