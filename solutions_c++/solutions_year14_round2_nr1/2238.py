#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>

#define abs(x) ((x)>0?(x):((-1)*(x)));

using namespace std;

class data {
    public:
    char alpha;
    int count;
};

int main() {
    int t;
    cin>>t;
    for(int x=1; x<=t; x++) {
        int n,i,j,num,ans;
        bool flag = 1;
        string a,b;
        data d1[100], d2[100];
        cin>>n;
        cin>>a>>b;
        memset(d1, 0, sizeof(d1));
        memset(d2, 0, sizeof(d2));

        char prev = a[0];
        d1[0].alpha = a[0];
        d1[0].count = 1;
        j = 0;
        for(i=1; i<a.length(); i++) {
            if(prev == a[i]) {
                d1[j].count++;
            }
            else {
                d1[++j].alpha = a[i];
                d1[j].count = 1;
                prev = a[i];
            }
        }

//        for(i=0; i<=j; i++) {
//            printf("d[%d].alpha = %c   d[%d].count = %d\n", i, d1[i].alpha, i, d1[i].count);
//        }

        num = j+1;

        prev = b[0];
        d2[0].alpha = b[0];
        d2[0].count = 1;
        j=0;
        for(i=1; i<b.length(); i++) {
            if(prev == b[i]) {
                d2[j].count++;
            }
            else {
                d2[++j].alpha = b[i];
                d2[j].count = 1;
                prev = b[i];
            }
        }

//        for(i=0; i<=j; i++) {
//            printf("d[%d].alpha = %c   d[%d].count = %d\n", i, d2[i].alpha, i, d2[i].count);
//        }

        if(num != (j+1)) {
            flag = 0;
            printf("Case #%d: Fegla Won\n", x);
            continue;
        }

        i=0;
        ans = 0;
        while(i<num) {
            if(d1[i].alpha!=d2[i].alpha) {
                flag = 0;
                break;
            }
            else {
                ans += abs(d1[i].count - d2[i].count);
            }
            i++;
        }

        if(flag) {
            printf("Case #%d: %d\n", x, ans);
        }
        else {
            printf("Case #%d: Fegla Won\n", x);
        }

    }
    return 0;
}
