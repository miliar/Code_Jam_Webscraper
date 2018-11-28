#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;


void main()
{
	int t;
	cin>>t;
	for(int ii=0; ii<t; ii++)
	{
		int n;
		vector<int> a;
		cin>>n;
		for(int i=0; i<n; i++)
		{
			int aa;
			cin>>aa;
			a.push_back(aa);
		}
		
		int cnt=0;
		while(!a.empty())
		{
			int p=min_element(a.begin(), a.end())-a.begin();
			cnt+=min(p, (int)a.size()-1-p);
			a.erase(a.begin()+p);
		}	

		cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
	}
}
