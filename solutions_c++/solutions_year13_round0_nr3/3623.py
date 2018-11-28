#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

#define epr(...) fprintf(stderr, __VA_ARGS__)

const int maxn = 1000;
const int inf = 1e9;


int a[maxn];

bool check(int x){
    bool flag;
    int j;
    for(j = 0; x; x /= 10){
	a[j++] = x % 10;
    }
    flag = 1;
    for(int k = 0; k < j / 2; k++)
	if (a[k] != a[j - k - 1])
	    flag = 0;
    return flag;
}

int main(){
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int t, cnt, l, r;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++){
	scanf("%d %d", &l, &r);
	cnt = 0;
	for(int i = l; i <= r; i++){
	    int d = sqrt(i);
	    if (d * d == i){
		
		if (check(d) && check(i)){
		    //epr("%d\n", i);
		    cnt++;
		}
	    }
	}
	printf("Case #%d: %d\n", tt + 1, cnt);
	
/*	x = i * i;
	for(j = 0; x; x /= 10)
	    a[j++] = x % 10;
	flag = 1;
	for(int k = 0; k < j / 2; k++)
	    if (a[k] != a[j - k - 1])
		flag = 0;
	if (flag) 
	    cout << i << " " << i * i << endl;*/
    }
    
    return 0;
}