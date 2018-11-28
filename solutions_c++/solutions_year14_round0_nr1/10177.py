#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int t,n1,n2,x,n=1;
	
	cin>>t;
	
	while(t--)
	{
		cin>>n1;
		vector<int> v1,v2;
		for(int i=1; i<n1; i++)
			for(int j=1; j<=4; j++)
				cin>>x;
		
		for(int j=1; j<=4; j++)
		{
			cin>>x;
			v1.push_back(x);
		}
		
		for(int i=n1+1; i<=4; i++)
			for(int j=1; j<=4; j++)
				cin>>x;
				
		cin>>n2;
		for(int i=1; i<n2; i++)
			for(int j=1; j<=4; j++)
				cin>>x;
		
		for(int j=1; j<=4; j++)
		{
			cin>>x;
			v2.push_back(x);
		}
		
		
		for(int i=n2+1; i<=4; i++)
			for(int j=1; j<=4; j++)
				cin>>x;
				
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
				
		int i=0,j=0,s = 0,v=0;
		while(i<4 && j<4)
		{
			if(v1[i] == v2[j])
			{
				v = v1[i];
				s++;
				i++;
				j++;
			}
			else if (v1[i] > v2[j])
				j++;
			else
				i++;
		}
		
		if(s > 1)
			cout<<"Case #"<<n<<": Bad magician!"<<endl;
		else if(s < 1)
			cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
		else
		{
			cout<<"Case #"<<n<<": "<<v<<endl;
		}
			
		n++;
	}
}
