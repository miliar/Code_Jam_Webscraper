#include<bits/stdc++.h>
using namespace std;

bool isComplete(int *a){
    int sum=0;
    for(int i=0;i<10;i++)
        sum+=a[i];
    if(sum==10) return true;
    return false;
}
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt;
    scanf("%d",&tt);
    for(int qq=1;qq<=tt;qq++){
        int i=0;
        long long n;
        int a[10]={0};
        scanf("%lld",&n);
        printf("Case #%d: ",qq);
        if(n==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        while(++i){
            long long nn=i*n;
            while(nn>0){
                a[nn%10]=1;
                nn/=10;
            }
            if(isComplete(a)) break;
        }
        cout<<i*n<<endl;
    }
    return 0;
}
