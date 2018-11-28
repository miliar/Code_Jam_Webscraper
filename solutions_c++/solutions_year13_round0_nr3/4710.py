#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int f[10000005];
void test(){
    char s[20];
    for(long long i = 1; i <= 10000000; i++){
        long long t = (long long)i*(long long)i;
        bool flag=true;
        sprintf(s,"%I64d",i);
        for(int j = 0,jj=strlen(s)-1; j<jj;j++,jj--)
            if(s[j]!=s[jj])flag=false;

        sprintf(s,"%I64d",t);
        for(int j = 0,jj=strlen(s)-1; j<jj;j++,jj--)
            if(s[j]!=s[jj])flag=false;

        if(flag)f[i]=true;
        else f[i]=false;
    }
}
int main(){
    int t,tt=1;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    test();
    scanf("%d", &t);
    while(t--){
        long long A,B;
        scanf("%I64d%I64d",&A,&B);
        long long AA = sqrt(A);
        long long BB = sqrt(B);
        int sum = 0;
        //printf("AA=%I64d BB=%I64d\n", AA, BB);
        for(long long i = AA; i <= BB; i++){
            if(f[i]&&i*i>=A&&i*i<=B){
                //printf("-------i*i=%I64d i=%I64d\n",i*i,i);
                sum++;
            }
        }
        printf("Case #%d: %d\n",tt++,sum);
    }
}

