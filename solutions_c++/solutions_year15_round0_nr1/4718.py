#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <climits>
#include <cfloat>
#include <cstdio>
#define x first
#define y second
#define IN(x, n) (0 <= (x) && (x) < n)
#define MAX 1010
#define MOD 1000000007
using namespace std;

int solve(int n, char s[]){
    int resp = 0, parados = 0;
    for(int i = 0; i <= n; i++){
        if(s[i] == '0')
            continue;
        if(parados<i){
            resp += i-parados;
            parados += (i-parados) + (s[i]-'0');
        }
        else
            parados += (s[i]-'0');
    }
    return resp;
}

int main(){
	int n, casos;
	char s[1010];
	scanf("%d", &casos);
	for(int i = 1; i <= casos; i++){
        scanf("%d%s", &n, s);
        printf("Case #%d: %d\n", i, solve(n, s));
	}
	return 0;
}
