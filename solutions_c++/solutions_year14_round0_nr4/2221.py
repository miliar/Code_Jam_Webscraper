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

int dwar (vector <double> Naomi , vector <double> Ken)
{
	reverse(all(Ken));
	int ans = sz(Naomi);
	
	for (int i=0 ; i<sz(Ken) ; i++)
	{
		int ind=-1;
		for (int j=0 ; j<sz(Naomi) ; j++)
		{
			if (Naomi[j] > Ken[i])
			{
				ind=j;
				break;
			}
		}

		if (ind == -1)
		{
			ind=0;
			ans--;
		}
		Naomi.erase(Naomi.begin()+ind);
	}
	
	return ans;
}

int main ()
{
	freopen("war.in","r",stdin);
	freopen("war.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	while (TC--)
	{		
		int N;
		cin >> N;
		
		vector <double> Naomi,Ken;
		
		for (int i=0 ; i<N ; i++)
		{
			double x;
			cin >> x;
			Naomi.pb(x);
		}
		
		for (int i=0 ; i<N ; i++)
		{
			double x;
			cin >> x;
			Ken.pb(x);
		}
		
		sort(all(Naomi));
		sort(all(Ken));

		int W=dwar(Ken,Naomi);
		int DW=dwar(Naomi,Ken);
		
		printf("Case #%d: %d %d\n",CC++,DW,N-W);
	}
	
}
