#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <fstream>
#include <string>
#include <cmath>
#include <queue>
 
using namespace std;
 
vector<vector<int> > a(4, vector<int>(4));


void read()
{
	for(int i = 0; i <4; i++)
		for(int j = 0; j <4; j++)
			cin>>a[i][j];
}
 
int main()
{
	//freopen("INPUT.TXT","r",stdin); freopen("OUTPUT.TXT","w",stdout);
	int t, f, l;
	vector<int> a1,a2;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>f;
		read();
		a1 = a[f-1];
		cin>>l;
		read();
		a2 = a[l-1];
		vector<int> res;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(a1[i] == a2[j])
					res.push_back(a1[i]);
		cout<<"Case #"<<i<<": ";
		if(res.size() > 1)
			cout<<"Bad magician!"<<endl;
		if(res.size() == 0)
			cout<<"Volunteer cheated!"<<endl;
		if(res.size() == 1)
			cout<<res[0]<<endl;
		
	}
	
}