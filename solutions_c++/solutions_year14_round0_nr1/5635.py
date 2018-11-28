#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 

#define pb push_back 
#define mp make_pair 
#define float long double 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 


int main(){ 
	
	int T;
	cin >> T;
	for(int qwe = 1; qwe <= T; qwe++)
			{
			
			int d[20], q;
			printf("Case #%d: ", qwe);
		for(int i = 1; i <= 16; i++)
		{
			d[i] = 0;
		}cin >> q;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				int x;
				cin >> x;
				if (i + 1 == q)
					d[x]++;
			}
		}	
		cin >> q;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				int x;
				cin >> x;
				if (i + 1 == q)
					d[x]++;
			}
		}	
		int cnt = 0;
		int ans = 0;
		for(int i =1; i <= 16; i++)
		{	
			if (d[i] == 2)
			{
				ans = i;
				cnt++;
			}
		}
		if (cnt == 1)
		{
			cout << ans << endl;
		} else if (cnt > 0)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
	
	
	return 0; 
} 
