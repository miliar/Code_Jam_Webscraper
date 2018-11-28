#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>

using namespace std;

#define For(i,a,b) for(typeof(a) i =(a);i<(b);i++)
#define ll long long
#define pb push_back
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(V) V.begin(),V.end()
/*****************************************************************************/
//
//char buf[10000];
//int main(){
//    int t;
//    scanf("%d",&t);
//    for(int cas=1;cas<=t;cas++){
//        int d;
//        scanf("%d",&d);
//        scanf("%s",buf);
//        string s = buf;
//        int tot=0,ret=0;
//        For(i,0,s.size()){
//            int x =s[i]-'0';
//            if (x==0) continue;
//            if (tot>=i){
//                tot+=x;
//            } else{
//                ret += i-tot;
//                tot += x+i-tot;
//            }
// //           cout << x << ' '<< i << ' '<< ret << ' '<< tot << endl;
//        }
////        cout << d << ' ' << s << ' ' << ret << endl;
//        printf("Case #%d: %d\n",cas,ret);
//    }
//    return 0;
//}
//


int a[10000];
int main(){

    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n;
        scanf("%d",&n);
        For(i,0,n){
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        int ret=a[n-1];
        For(i,2,a[n-1]+1){
            int count=0;
            int j=n-1;
            while (j>=0 && a[j]>i){
                count+=(a[j]+i-1)/i -1;
                j--;
            }
            //cout << i << ' '<< count << endl;
            ret = min(ret,count+i);
        }
        printf("Case #%d: %d\n",cas,ret);
    }
    return 0;
}
