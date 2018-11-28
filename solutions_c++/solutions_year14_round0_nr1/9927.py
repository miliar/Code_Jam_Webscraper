#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int k=1; k<=t; k++)
	{
		int r=2;
	//	while(r--)
	//	{
			int n,n1,a;
			cin >> n;
			vector<int>v1,v2;
			for(int i=1; i<=4; i++)
			{
				if(i == n)
				{
					//cout << i << " " << n << endl;
					for(int j=0; j<4; j++)
					{
						cin >> a;
						v1.push_back(a);
						//cout << "SF";
					}
				}
				else
				{
					for(int j=0;j<4; j++)
					{
						cin >> a;
					}
				}
			}
		//} 
			cin >> n1;
			for(int i=1; i<=4; i++)
			{
				if(i == n1)
				{
					for(int j=0; j<4; j++)
					{
						cin >> a;
						v2.push_back(a);
					}
				}
				else
				{
					for(int j=0;j<4; j++)
					{
						cin >> a;
					}
				}
			}
		
			int c=0,f=0,num;
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
				{
					if(v1[i] == v2[j])
					{
						c++;
						if(f==0)
						{
							num = v2[j];
							f=1;
						}
					}	
				}
			}
			if(c == 1)	
			{
				cout << "Case #"<<k <<": "<<num << endl;
			}
			else if(c>=2)
			{
				cout << "Case #"<<k <<": Bad magician!\n";
			}
			else if(c == 0)
			{
				cout << "Case #"<<k <<": Volunteer cheated!\n";
			}
	}
	return 0;
}
