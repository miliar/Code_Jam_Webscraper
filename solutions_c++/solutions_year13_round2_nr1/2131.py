#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <memory.h>
#include <string.h>
//#include <assert.h>
using namespace std;

#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define inf 1100000000
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int t, n, A, x;
vector<int> motes;

int main(){
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	scanf("%d", &t);
	FOR(tt,1,t){
		scanf("%d %d", &A, &n);
		motes.clear();
		FOR(i,1,n){
			scanf("%d", &x);
			motes.pb(x);
		}
		sort(all(motes));
		int cur = A;
		int oper = 0;
		int operadd = 0;
		FOR(i,0,n-1){
			if(motes[i] < cur){
				cur += motes[i];
			}else{
				if(cur == 1){
					oper += n-i;
					break;
				}else{
					operadd = 0;
					while(motes[i] >= cur){
						cur += cur-1;
						operadd++;
					}
					if(operadd < n-i){
						oper += operadd;
						cur += motes[i];
					}else{
						oper += n-i;
						break;
					}
				}
			}
		}

		cout << "Case #" << tt << ": " << oper << endl;
	}

	return 0;
}