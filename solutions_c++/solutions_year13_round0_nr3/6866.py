#include <iostream>
using namespace std;
int main(){
    freopen("C:\\Users\\Administrator\\Downloads\\C-small-attempt0.in","r",stdin);
    freopen("C:\\out.out","w",stdout);
    int n,i,j,k,tt;
    int t[10];
    int a[1010],b[1010];
    for(i=0;i<1010;i++){
        a[i]=b[i]=0;
    }
    for(i=1;i<=1000;i++){
        int ii=i;
        k=0;
        while(ii){
            t[k]=ii%10;
            ii/=10;
            k++;
        }
        for(j=0;j<k;j++){
            if(t[j]!=t[k-j-1])break;
        }
        if(j==k){
            a[i]=1;
            if(i*i<1010){
                b[i*i]=1;
            }
        }
    }
    cin>>n;
    for(tt=1;tt<=n;tt++){
        cin>>i>>j;
        int ret=0;
        for(;i<=j;i++){
            if(a[i]==1&&b[i]==1){
                cout<<i<<endl;
                ret++;
            }
        }
        printf("Case #%d: %d\n",tt,ret);
    }
    return 0;
    //while(1);
}
