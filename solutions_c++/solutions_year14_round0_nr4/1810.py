#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>
using namespace std;
int main(){
  freopen("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int uu=0;uu<t;uu++){
        int n;
        scanf("%d",&n);
        vector<double> a,b,c,d;
        double temp;
        for(int i=0;i<n;i++){
                scanf("%lf",&temp);
                a.push_back(temp);
                c.push_back(temp);
        }
        for(int i=0;i<n;i++){
                scanf("%lf",&temp);
                b.push_back(temp);
                d.push_back(temp);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        sort(c.begin(),c.end());
        sort(d.begin(),d.end());
        int c1 = 0;
        int c2 = 0;
        for(int i=0;i<n;i++){
            if(a[0]>b[0]){
                c1++;
                a.erase(a.begin());
                b.erase(b.begin());
            }
            else{
                a.erase(a.begin());
                b.erase(b.begin()+n-i-1);
            }
        }
        for(int i=0;i<n;i++){
            if(c[n-i-1]>d[n-i-1]){
                c.erase(c.begin()+n-i-1);
                d.erase(d.begin());
                c2++;
            }
            else{
                c.erase(c.begin()+n-i-1);
                d.erase(d.begin()+n-i-1);
            }
        }
        printf("Case #%d: %d %d\n",uu+1,c1,c2);
    }
    return 0;
}
