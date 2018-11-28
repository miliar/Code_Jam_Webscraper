#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
long long gcd(long long A,long long B)
{
    if(B>A)  swap(A,B);
   if(A%B==0)
      return B;
   else return gcd(A%B,B);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,it,i;
    long long P,Q,Ans;
    char str[100];
    scanf("%d",&T);
    for(it=1; it<=T; it++)
    {
        scanf("%s",str);
        P=Q=0;
        int l=strlen(str);
        for(i=0; str[i]!='/'; i++)
        {
            P*=10;
            P+=str[i]-'0';
        }
        i++;
        for(; i<l; i++)
        {
            Q*=10;
            Q+=str[i]-'0';
        }
        long long G=gcd(P,Q);
        P/=G;Q/=G;
       // cout<<P<<" "<<Q<<endl;
       if(P==1 && Q==1){
           printf("Case #%d: ",it);
           printf("0\n");
           continue;
       }
       long long m=1;
       bool f=false;
        for(i=1;m<=Q ; i++){
            m*=2;
            if(m==Q){
                f=true;
                break;
            }
        }
        printf("Case #%d: ",it);
        if(!f){
                printf("impossible\n");
                continue;
        }
        Ans=0;
        while(1){
            Ans++;
            if(P*2>=Q){
                break;
            }
            else Q/=2;
        }
        printf("%d\n",Ans);
    }
    return 0;
}
