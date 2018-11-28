#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;

typedef long long llong;

VI V1, V2;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int TC;
  cin>>TC;

  for(int j = 1; j <= TC; j++)
  {
  	V1.clear();
  	V2.clear();
  	set<int> ST;

  	int row;
  	cin>>row;
  	row--;

  	for(int k=0; k < 4; k++)
  	{
  		for(int i=0; i < 4; i++)
  		{
  			int n; 
  			cin>>n;

  			if(row == k)
  			{
  			//	cout<<n<<" ";
  				V1.push_back(n);
  				ST.insert(n);
  			//	cout<<endl;
  			}
  		}
  	}

  	cin>>row;
  	row--;

  	for(int k=0; k < 4; k++)
  	{
  		for(int i=0; i < 4; i++)
  		{
  			int n; 
  			cin>>n;
  			
  			if(row == k)
  			{
  			//	cout<<n<<" ";
  				V2.push_back(n);
  				ST.insert(n);
  			//	cout<<endl;
  			}

  		}
  	}

  	//cout<<ST.size()<<endl;

  	if(ST.size() > 7)
  		cout<<"Case #"<<j<<": Volunteer Cheated!"<<endl;
  	else if(ST.size() < 7)
  		cout<<"Case #"<<j<<": Bad magician!"<<endl;	
  	else
  	{

  		for(int k=0; k < 4;k++)
  		{
  			for(int i=0; i < 4; i++)
  			{
  				if(V1[k] == V2[i])
  					cout<<"Case #"<<j<<": "<<V1[k]<<endl;	
  			}
  		}

  	}
  }
  
  return 0;
}



