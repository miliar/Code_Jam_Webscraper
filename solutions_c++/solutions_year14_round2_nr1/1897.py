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
	freopen("A_small.in","r",stdin);
	freopen("A_small.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	while (TC--)
	{
		int N;
		cin >> N;
		string a,b;
		cin >> a >> b;
		int ret=0;
		bool OK=1;
		
		int i=0,j=0;
		
		while (1)
		{
			if (a == b) break;
			if (i == sz(a) || j == sz(b))
			{
				OK=0;
				break;
			}
			if (a[i] != b[j])
			{
				OK=0;
				break;
			}
			
			int cnt1=0 , cnt2=0;
			for (int k=i ; a[k]==a[i] && k<sz(a) ; k++) cnt1++;
			for (int k=j ; b[k]==a[i] && k<sz(b) ; k++) cnt2++;
			
			if (cnt1 < cnt2)
			{
				string s;
				for (int k=0 ; k<cnt2-cnt1 ; k++) s+=a[i];
				a.insert(i,s);
			}
			if (cnt2 < cnt1)
			{
				string s;
				for (int k=0 ; k<cnt1-cnt2 ; k++) s+=a[i];
				b.insert(i,s);
			}
			//cout << cnt1 << " " << cnt2 << endl;
			i += max(cnt1,cnt2);
			j += max(cnt1,cnt2);
			
			ret += abs(cnt1-cnt2);
			//cout << a << " " << b << endl;
		}
		printf("Case #%d: ",CC++);
		if (!OK) cout << "Fegla Won" << endl;
		else cout << ret << endl;
	}
	
}
