#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
using namespace std;

 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef long long ll;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

int main ()
{
	freopen("magic.in","r",stdin);
	freopen("magic.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	while (TC--)
	{
		int r1,r2;
		map <int,int> m;
		
		cin >> r1;
		
		for (int i=0 ; i<4 ; i++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				int x;
				cin >> x;
				if (i == r1-1) m[x]++;
			}
		}
		
		cin >> r2;
		
		for (int i=0 ; i<4 ; i++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				int x;
				cin >> x;
				if (i == r2-1) m[x]++;
			}
		}
		
		map <int,int>::iterator it;
		vi v;
		
		for (it=m.begin() ; it!=m.end() ; it++)
		{
			if (it->second == 2) v.pb(it->first);
		}
		
		printf("Case #%d: ",CC++);
		if (v.empty()) cout << "Volunteer cheated!" << endl;
		else if (v.size() > 1) cout << "Bad magician!" << endl;
		else cout << v[0] << endl;
	}
	
}
