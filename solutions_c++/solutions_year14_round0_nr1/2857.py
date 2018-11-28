#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

#define type long long

using namespace std;

int main()
{

  cin.tie(NULL);
  std::ios::sync_with_stdio(false);

  int t;
  cin>>t;
  int cas = 0;
  while(t--)
  {
  	int tab[2];

  	vector<int> v[2];
  	vector<int> res(4);

  	for(int r=0; r<2; r++)
  	{
  		cin>>tab[r];
 		for(int i=0; i<4; i++)
  				for(int j=0; j<4; j++)
  				{
  					int temp;
  					cin>>temp;
  					if(i == tab[r]-1)
  						v[r].push_back(temp);
  				}
  	}

  	sort(v[0].begin(), v[0].end());
  	sort(v[1].begin(), v[1].end());


  	vector<int>::iterator it = set_intersection (v[0].begin(), v[0].end(), v[1].begin(), v[1].end(), res.begin());
  	res.resize(it-res.begin());  
  	
  	cas++;
  	cout<<"CASE #"<<cas<<": ";


  	if(res.size() == 1)
  		cout<<res[0]<<"\n";
  	if(res.size() == 0)
  		cout<<"Volunteer cheated!\n";
  	if(res.size() > 1)
  		cout<<"Bad magician!\n";
  }

  return 0;
 
}