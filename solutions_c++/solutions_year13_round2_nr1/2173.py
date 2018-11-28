#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct aa{
    int shi,mo;
    int bu;
    int zhi;
};
int main(){
    int t;
    scanf("%d",&t);
    for(int iiii=1;iiii<=t;iiii++){
        int zhi,n;
        scanf("%d%d",&zhi,&n);
        int i;
        int a[n];
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        queue<struct aa> q;
        struct aa temp,tt;
        temp.shi=0;
        temp.mo=n-1;
        temp.zhi=zhi;
        temp.bu=0;
        q.push(temp);
        int min=1000;
        while(!q.empty()){
            tt.shi=q.front().shi;
            tt.mo=q.front().mo;
            tt.zhi=q.front().zhi;
            tt.bu=q.front().bu;
            q.pop();
            if(tt.zhi>a[tt.shi]){
                tt.zhi+=a[tt.shi];
                tt.shi++;
                if(tt.shi>tt.mo)
                    min=min<tt.bu?min:tt.bu;
                else
                    q.push(tt);
            }
            else{
                tt.bu++;
                tt.mo--;
                if(tt.shi>tt.mo)
                    min=min<tt.bu?min:tt.bu;
                else
                    q.push(tt);
                if(tt.zhi!=1){
                    tt.mo++;
                    tt.zhi=tt.zhi*2-1;
                    q.push(tt);
                }
            }
        }
        printf("Case #%d: %d\n",iiii,min);
    }
}