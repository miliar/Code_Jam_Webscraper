#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
int main()
{
    int t,i;
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    scanf("%d",&t);
    char arr[1002];
    for(int k=1;k<=t;k++){
        int n,ans=0,p=0,dif=0;
    scanf("%d %s",&n,&arr);
    p=arr[0]-48;
   for(i=1;i<=n;i++){
    if(p>=i){
        p=p+(arr[i]-48);
    }
    else if(p<i && arr[i]!=48){
        dif=i-p;
        ans+=dif;
        p=p+dif+(arr[i]-48);
    }
   }
   printf("Case #%d: %d\n",k,ans);
    }

    return 0;
}
