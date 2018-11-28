#include<bits/stdc++.h>

using namespace std;


int main(){

    int T,cs,n,i,len,arr[1005],tot,cnt,diff;
    char a[1005];

    scanf("%d", &T);

    for(cs=1;cs<=T;cs++){
        scanf("%d %s",&n,a);
        len = strlen(a);
        cnt=0;
        for(i=0;i<len;i++)
            arr[i]=a[i]-48;
        tot=arr[0];
        for(i=1;i<len;i++){
            if(tot>=i) tot+=arr[i];
            else if(arr[i]!=0){
                diff = i-tot;
                cnt+=diff;
                tot+=(diff+arr[i]);
            }
        }

        printf("Case #%d: %d\n",cs,cnt);
    }

    return 0;
}
