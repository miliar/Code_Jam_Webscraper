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
	freopen("B_small.in","r",stdin);
	freopen("B_small.out","w",stdout);

	int TC;
	cin >> TC;
	int CC=1;
	while (TC--)
	{
		int A,B,K;
		cin >> A >> B >> K;
		
		ll cnt=0;
		for (int i=0 ; i<A ; i++)
		{
			for (int j=0 ; j<B ; j++)
				if ((i&j) < K)
				{
					//cout << i << " " << j << endl;
					cnt++;
				}
		}
		
		printf("Case #%d: %lld\n",CC++,cnt);
	}		
}
