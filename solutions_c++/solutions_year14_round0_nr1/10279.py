#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <iterator>

using namespace std;
int arr[5][5];
int main() {
	freopen("A-small-attempt2.in","r",stdin);
	freopen("a.out","w+",stdout);
	int t;
	cin>>t;
	for(int p = 1;p<=t;p++)
	{
		int first;
		cin>>first;
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
				cin>>arr[i][j];
		set<int> seta;
		for(int i=1;i<5;i++)
			seta.insert(arr[first][i]);
		int second;
		cin>>second;
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
				cin>>arr[i][j];
		set<int> setb;
		for(int i=1;i<5;i++)
			setb.insert(arr[second][i]);
		set<int> setc;
		set_intersection(seta.begin(),seta.end(),setb.begin(),setb.end(),inserter(setc, setc.begin()));
		cout<<"Case #"<<p<<": ";
		if(setc.size()>1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else if(setc.size()==1)
		{
			set<int>::iterator it = setc.begin();
			cout<<*it<<endl;
		}
		else
			cout<<"Volunteer cheated!"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
