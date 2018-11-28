#include <iostream>
#include <stdio.h>
using namespace std;

freopen("A-small-attempt0.in","r",stdin);
freopen("Program1.out","w",stdout);

int a[10];

void func(long long int x){
    int r;
    while(x!=0){
        r=x%10;
        a[r]=1;
        x/=10;
    }
    return;
}
int main() {
    int t,i,j,sum;
    long long int n,temp;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%lld",&n);
        for(j=0;j<10;j++)
            a[j]=0;
        if(n==0){
            printf("Case #%d: INSOMNIA \n",i+1);
            continue;
        }
        temp=n;
        while(1){
            sum = 0;
            func(temp);
            for(j=0;j<10;j++)
                sum+=a[j];
            if(sum==10)
                break;
            temp+=n;;
        }
        printf("Case #%d: %lld \n",i+1,temp);
    }
	return 0;
}
