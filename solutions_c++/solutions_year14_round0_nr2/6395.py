#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
double t,c,f,x;
int main() {
   freopen("B-large.in", "r" , stdin);
   freopen("output.txt" , "w" , stdout);
    while(cin>>t) {
        int tcase=0;
        while(t--) {
            cin>>c>>f>>x;
            double sum=0.0;
            double curtime=2;
            while(1) {
                if(sum+x/curtime<=sum+c/curtime+x/(curtime+f)) {
                    sum+=x/curtime;
                    break;
                } else {
                    sum+=c/curtime;
                    curtime+=f;
                }
            }
            printf("Case #%d: ",++tcase);
            printf("%.7f\n",sum);
        }
    }
    return 0;
}
