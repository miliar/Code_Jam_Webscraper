
#define LOCAL
#include <stdio.h>
#include <string.h>
#include <math.h>
int a[10000005];
int main(){
#ifdef LOCAL
       freopen("data.txt", "r", stdin);
       freopen("data.out", "w", stdout);
#endif
       int t,n;
       void init();
       init();
       scanf("%d",&t);
       for(n=1;n<=t;n++){
                         printf("Case #%d: ",n);
                         void work();
                         work();
                         }
       return 0;    
}
int Palindrome(char st[1000]){
    int r=strlen(st)-1;
    int l=0;
    while(l<r){
               if(st[l]!=st[r])
               return 0;
               l++;r--;
               }
    return 1;
}    
void init(){
     long long i=0;
     for(i=0;i<=10000001;i++){
     char st1[1000],st2[1000];
     sprintf(st1,"%I64d",i);
     sprintf(st2,"%I64d",i*i);
     
     if(Palindrome(st2)&&Palindrome(st1)){a[i]=1;}
     }
     for(i=1;i<=10000001;i++)a[i]+=a[i-1];
}
void work(){
     long long i,l,r;
     scanf("%I64d%I64d",&l,&r);
     l--;
     long long rr=sqrt(r)+2;
     while(rr*rr>r)rr--;
     long long ll=sqrt(l)+2;
     while(ll*ll>l)ll--;
     printf("%d\n",a[rr]-a[ll]);
}
