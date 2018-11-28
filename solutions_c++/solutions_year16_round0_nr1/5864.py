#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <fstream>
#include <stack>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;

int a[15],sum[15],s[10];

int main(){
    int t,n,kase=0;
    cin>>t;
    while (t--) {
        kase++;
        cin>>n;
        memset(a, 0, sizeof(a));
        memset(sum, 0, sizeof(sum));
        memset(s, 0, sizeof(s));
        int flag=log10(n),maxx=flag;
        printf("Case #%d: ",kase);
        if (n==0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for (int i=0; i<=flag; i++) {
            a[i]=n%10;
            n/=10;
        }
        int sig=0;
        while (sig<10) {
            for (int i=0; i<=maxx; i++) {
                sum[i]+=a[i];
                if (sum[i]>=10) {
                    sum[i+1]++;
                    sum[i]%=10;
                }
                if (s[sum[i]]==0) {
                    sig++;
                    s[sum[i]]=1;
                }
            }
            if (sum[maxx+1]>0) {
                maxx++;
                if (s[sum[maxx]]==0) {
                    s[sum[maxx]]=1;
                    sig++;
                }
            }
        }
        for (int i=maxx; i>=0; i--) {
            cout<<sum[i];
        }
        cout<<endl;
    }
    return 0;
    
}
