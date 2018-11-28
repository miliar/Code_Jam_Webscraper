#include<stdio.h>
#include<algorithm>
using namespace std;
int dg[10];
char in1[20],in2[20];
int ans1,ans2,minn,n;
int csum() {
    int a=0,b=0;
    for(int i=0;i<n;i++) {
        a*=10;
        b*=10;
        a+=in1[i]-'0';
        b+=in2[i]-'0';

    }
    int tmp = (a<b? b-a:a-b);
    if(tmp < minn) {
        minn = tmp;
        ans1 = a;
        ans2 = b;
    } else if(tmp == minn) {
        if(a<ans1) {
            ans1 = a;
            ans2 = b;
        }
        else if(a==ans1 && b<ans2) {
            ans1 = a;
            ans2 = b;
        }
    }
}
void calc(int a,int b) {
    if(a >= n && b>=n) {
        csum();
        //printf("%d%d %d%d\n",in1[n-2]-'0',in1[n-1]-'0',in2[n-2]-'0',in2[n-1]-'0');
        return ;
    }
    if(a>=n) {
        if(in2[b] == '?') {
            for(int i=0;i<=9;i++) {
                in2[b] = i+'0';
                calc(a,b+1);
            }
            in2[b] = '?';
        } else {
            calc(a,b+1);
        }
        return ;
    }
    if(in1[a] == '?') {
        for(int i=0;i<=9;i++) {
            in1[a] = i+'0';
            calc(a+1,b);
        }
        in1[a] = '?';
    }
    else {
        calc(a+1,b);
    }

}
int main(){
    int t,i,j,k;

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    scanf("%d",&t);

    for(k=1;k<=t;k++) {
        scanf("%s %s",in1,in2);
        minn = 19999999;
        for(n=0;in1[n]!='\0';n++);
        //printf("n = %d\n",n);
        calc(0,0);


        printf("Case #%d: ",k);
        int tmp=1;
        for(i=1;i<n;i++) {
            tmp*=10;
        }
        while(tmp>ans1) {
            printf("0");
            tmp/=10;
        }
        if(ans1>0)printf("%d",ans1);
        printf(" ");

        tmp=1;
        for(i=1;i<n;i++) {
            tmp*=10;
        }
        while(tmp>ans2) {
            printf("0");
            tmp/=10;
        }
        if(ans2>0)printf("%d",ans2);
        printf("\n");
        //printf("%d %d\n",ans1,ans2);
    }
}
