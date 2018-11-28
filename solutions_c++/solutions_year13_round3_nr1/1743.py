#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
int main() {
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    scanf("%d",&t);
    int k=0;
    while(t--) {
        k++;
        string a;
        int f;
        cin>>a>>f;
        int ans=0;
        for(int i=0; i<a.length(); i++) {
            for(int j=i; j<a.length(); j++) {
                int count=0;
                for(int ia=i; ia<=j; ia++) {
                   // cout<<a[ia];
                    if(a[ia]=='a'||a[ia]=='e'||a[ia]=='i'||a[ia]=='o'||a[ia]=='u')
                        count=0;
                    else
                        count++;
                    if(count==f) {
                        ans++;
                        break;
                    }
                }
                //cout<<endl;

            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
}
