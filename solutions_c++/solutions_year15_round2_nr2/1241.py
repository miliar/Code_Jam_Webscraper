/**
 * Md Imran Hasan Hira (imranhasanhira@gmail.com)
 */

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int T, r, c, n;

int bc(int p){
    int res=0;
    while(p){
        if(p&1) res++;
        p  = (p>>1);
    }
    return res;
}

bool has(int x, int a, int b){
    return (1 << a*c+b ) & x;
}

int calc(int x){
    int res=0;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if( i>0 && has(x, i,j) && has(x, i-1, j)) res++;
            if( j>0 && has(x, i,j) && has(x, i, j-1)) res++;
        }
    }
    return res;
}

int main(){
    freopen("B-small-attempt1.in", "r", stdin);
    //freopen("b.in", "r", stdin);
    freopen("bout.txt", "w", stdout);

    cin >> T;
    for(int test=1;test<=T;test++){
        cin >> r >> c >> n;

        int g = r*c;
        //cout << g << endl;
        g =  (1 << g) ;
        //printf("%x \n", g);
        int res=99999999;
        for(int i=0;i<g;i++){
            int num = bc(i);
            //cout << i << " " << num << endl;
            if(num == n) res = min(res, calc(i));
        }
        printf("Case #%d: %d\n", test, res);
    }
    return 0;
}
