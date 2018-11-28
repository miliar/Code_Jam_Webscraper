#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <string.h>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#define LIMIT 100
using namespace std;
int cs,need,maxi,stand,a[LIMIT];
string s;
int main(){
    cin >> cs;
    for(int t=1;t<=cs;t++){
        cin >> maxi ;
        cin >> s ;
        for(int i=0;i<=maxi;i++){
            a[i]=s[i]-'0';
        }
        stand=a[0];
        need=0;
        for(int i=1;i<=maxi;i++){
            if(a[i]==0){
                continue;
            }
            if(stand<i){
                need += ( i - stand ) ;
                stand += ( i - stand ) ;
            }
            stand += a[i];

        }
        printf("Case #%d: %d\n",t,need);
    }
}
