#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <map>

#define LL long long
#define pii pair<int, int>

using namespace std;

bool palin(long long x) {
     long long a=x;
     long long y=0;
     while (a!=0LL) {
           y=y*10LL+a%10LL;
           a=a/10LL;
     }
     if (x==y) return true; else return false;
}

int main() {
    
    vector <int> vec;
    for (int i=1;i<=10000000;i++) {
        long long tes=(LL)i*i;
        if (palin(i) && palin(tes)){
           vec.push_back(i);
        }
    }//printf("%d\n",vec.size());
    int ntc;
    scanf("%d",&ntc);
    long long wow,a,b;
    for (int tc=1;tc<=ntc;tc++) {
        scanf("%lld %lld",&a,&b);
        int jum=0;
        for (int i=0;i<vec.size();i++) {
            wow=(LL)vec[i]*vec[i];
            if (wow>=a && wow<=b) {jum++;}
            if (wow>b) break;
        }
        printf("Case #%d: %d\n",tc,jum);
    }
    return 0;
}
