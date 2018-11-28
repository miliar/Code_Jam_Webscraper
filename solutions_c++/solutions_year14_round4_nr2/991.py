#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

int t, l[1005], r[1005], ans, n;
bool dir[1005];
map<int, int> m;

int main(){
    //cout << "test";
    freopen("input.txt", "r", stdin);
    freopen("output.out", "w", stdout);
	scanf("%d", &t);
	for(int k = 1; k <= t; ++k){
		scanf("%d", &n);
		m.clear();
		ans = 0;
		for(int a = 0; a < n; ++a){
			scanf("%d", &l[a]);
            r[a] = l[a];
			m[l[a]] = a;
		}
		sort(l, l+n);
		for(int a = 0; a < n; ++a){
            int left = 0, right = 0;
            int pos = m[l[a]];
            int cur = l[a];
            //cout << cur << " " << pos << endl;
            for(int b = 0; b < pos; ++b){
                if(r[b] < cur){
                    //if(dir[b] == true) ++left;
                    ++left;
                }
            }
            for(int b = pos+1; b < n; ++b){
                if(r[b] < cur){
                    //if(dir[b] == false) ++right;
                    ++right;
                }
            }
            //cout << cur << " " << pos << " " << left << " " << right << endl;
            int one = pos - left;
            int two = n - pos - 1 - right;
            //cout << m[l[a]] << " " << le << " " << r << endl;
			if(one <= two){
				ans += one;
                dir[pos] = false;
			}
			else{
                ans += two;
                dir[pos] = true;
			}
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
