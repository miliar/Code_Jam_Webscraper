#include <iostream>
#include <stdio.h>
#include <algorithm>
#define ll long long
#define maxn 100010
using namespace std;
int N, T;
string st;
int main(){
    cin >> T;
    for (int _ = 1; _ <= T; _++){
    	cin >> N >> st;
    	int ct = 0 , ans = 0;
    	for (int i=0;i<st.size();i++){    		
    		if (st[i]=='0') continue;
    		ans = max (ans , i - ct);
    		ct += st[i]-'0';
    	}
        printf("Case #%d: %d\n", _ , ans);
    }
    return 0;
}