#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

#define si(x) scanf("%d", &x)
#define sii(x, y) scanf("%d%d", &x, &y)
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define FORI(i, n, m) for(int i = (n); i < (m); i++)

typedef long long int64;

char shyness[1003];

int main(){
    int t;
    si(t);
    FOR(T, t){
		int s;
		si(s);
		s++;
		scanf("%s", shyness);
		int additional = 0, standing = 0;
		FOR(i, s){
			if(standing < i){
				additional += i - standing;
				standing = i;
			}
			standing += shyness[i] - '0';
		}
		printf("Case #%d: %d\n", T+1, additional);
	}
    return 0;
}