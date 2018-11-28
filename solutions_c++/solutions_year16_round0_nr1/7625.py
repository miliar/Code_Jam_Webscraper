#include <bits/stdc++.h>
#define ll long long
//subhajit gorai
using namespace std;
int arr[10];
int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++){
        ll n;
        scanf("%lld",&n);
        memset(arr,0,sizeof(arr));
        if(n==0){
            printf("Case #%d: INSOMNIA\n",z);
            continue;
        }
        int c=10;
        ll i=1,num;
        while(1){
            num=n*i;
            i++;
            //cout<<num<<"  "<<c<<endl;
            while(num!=0){
                int d=num%10;
                num=num/10;
                if(arr[d]==0){
                    arr[d]++;
                    c--;
                }
            }
            if(c==0){
                printf("Case #%d: %lld\n",z,n*(i-1));
                break;
            }
        }
    }
    return 0;
}
