#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define pb push_back
#define x first
#define y second

using namespace std;

typedef long long int tint;
typedef pair<int,int> par;

bool vowel(char c)
{
	return ( (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u') );
}

int main()
{
	int t,n;
	string name;
	tint res;
	cin >> t;
	vector<int> pos;
	bool grupo;
	forn(caso,t){
		res = 0;
		pos.clear();
		cin >> name >> n;
		int l = name.size();
		forn(i,l-n+1){
			if(not(vowel(name[i]))){
				grupo = true;
				forsn(j,i,i+n){		
					grupo = grupo and not(vowel(name[j]));
				}
				if(grupo){
					pos.pb(i);
				}
			}
		}

		forsn(i,n-1,l){
			int low = lower_bound (pos.begin(), pos.end(), i) - pos.begin();
			if(low == pos.size()) low--;
			while(low >= 0){
				if((pos[low]+n-1) > i) low--;
				else break;
			}
			if(low >= 0){
				int pri = pos[low];
				if( (pri + n - 1) <= i ){
					res += (tint)(pri+1);
					//cout << i << ": " << res << endl;
				}
			}
		}

		cout << "Case #" << (caso+1) << ": " << res << endl;
	}
	return 0;
}
