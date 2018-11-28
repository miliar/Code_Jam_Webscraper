//HARE KRISHNA
#include<bits/stdc++.h>
using namespace std;

#define ll long long
int main(){
    freopen("input3.in","r",stdin);
    freopen("out3.txt","w",stdout);
    int t,tcase;
    scanf("%d",&t);
    char str[105];
    int arr[105];
    for(tcase=1;tcase<=t;tcase++){
        scanf("%s",str);
        int len=strlen(str);
        int i;
        for(i=1;i<=len;i++){
            if(str[i-1]=='+'){
                arr[i]=1;
            }
            else{
                arr[i]=0;
            }
        }
        ll step=0;
        while(1){
            int which=arr[1];
            int cnt=0;
            for(i=1;i<=len;i++){
                if(arr[i]==which){
                    cnt++;
                }
                else break;
            }
            if(cnt==len && which==1)break;
            if(arr[1]==1){
            for(i=1;i<=cnt;i++){
                arr[i]=0;
            }
            }
            else{
                for(i=1;i<=cnt;i++){
                    arr[i]=1;
                }
            }
            step++;
        }
        printf("Case #%d: %lld\n",tcase,step);
    }
    return 0;
}
