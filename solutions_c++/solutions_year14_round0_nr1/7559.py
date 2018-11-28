#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main() 
{
	int n,c=1;
	cin>>n;
	for(int z=0; z<n; z++)
	{
		int mat1[4][4];
		int mat2[4][4];
		int n1,n2, vc;
		vector< vector<int> > v1;
		vector< vector<int> > v2;
		vector<int> resp;
		
		cin>>n1;
		for(int i=0; i<4; i++)
		{
			vector<int> v;
			for(int j=0; j<4; j++)
			{
				cin>>vc;
				v.push_back(vc);
			}
			v1.push_back(v);
		}

		cin>>n2;
		for(int i=0; i<4; i++)
		{
			vector<int> v;			
			for(int j=0; j<4; j++)
			{
				cin>>vc;
				v.push_back(vc);
			}
			v2.push_back(v);
		}

		vector<int>::iterator it;
		vector<int> vt = v2.at(n2-1);
		for(int j=0; j<4; j++)
		{
			int val = v1.at(n1-1).at(j);
			it = find(vt.begin(), vt.end(), val);
			if(it!=vt.end())
				resp.push_back(*it);
		}

		if(resp.size() == 1)
		{
			cout<<"Case #"<<c<<": "<<resp.at(0)<<endl;
		}
		else if(resp.size() > 1)
		{
			cout<<"Case #"<<c<<": Bad magician!"<<endl;
		}
		else if(resp.size() == 0)
		{
			cout<<"Case #"<<c<<": "<<"Volunteer cheated!"<<endl;
		}
		c++;
	}

	return 0;
}