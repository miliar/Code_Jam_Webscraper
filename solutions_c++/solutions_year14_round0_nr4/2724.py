#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
#define eps 1e-8
int main()
{
    int T,n,j,i,cas=1;
    double tt;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        vector<double> v1,v2,v3,v4;
        for (i=0;i<n;i++){
            scanf("%lf",&tt);
            v1.push_back(tt);
            v3.push_back(tt);
        }
        for (i=0;i<n;i++){
            scanf("%lf",&tt);
            v2.push_back(tt);
            v4.push_back(tt);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        sort(v3.begin(),v3.end());
        sort(v4.begin(),v4.end());
        int ans1=0,ans2=0;
        for (i=0;i<n;i++){
            if (v1[0]<v2[0]) {
                v1.erase(v1.begin());
                v2.pop_back();
            }else{
                v1.erase(v1.begin());
                v2.erase(v2.begin());
                ans1++;
            }
        }
        for (i=0;i<n;i++){
            for (j=0;j<v4.size();j++){
                if (v4[j]>v3[0]) break;
            }
            if (j<v4.size()){
                v4.erase(v4.begin()+j);
                v3.erase(v3.begin());
            }else{
                ans2++;
                v4.erase(v4.begin());
                v3.erase(v3.begin());
            }
        }
        printf("Case #%d: %d %d\n",cas++,ans1,ans2);
    }
    return 0;
}
