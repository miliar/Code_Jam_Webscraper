#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int a[10];
int num;
void count(int n){
    while(n>0){
        int t=n%10;
        if(a[t]==0){
            a[t]=1;
            num++;
        }
        n=n/10;
    }
}

int main(){
    freopen("test.txt", "r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        num=0;
        int m;
        int flag=1;
        int ii=1;
        memset(a, 0, sizeof(a));
        scanf("%d",&m);
        while(num!=10){
            count(ii*m);
            ii++;
            if(m==0){
                flag=0;
                break;
            }
        }
        if(flag==0){
            printf("Case #%d: INSOMNIA\n",i);
        }
        else{
            printf("Case #%d: %d\n",i,(ii-1)*m);
        }
    }
}