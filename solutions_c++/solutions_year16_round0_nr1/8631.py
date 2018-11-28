#include <bits/stdc++.h>
#define pr(l) printf("Case #%d: ",l)
#define mod 1000000007
#define Int long long int
using namespace std;
 int main(){
    freopen("alarge.in","r",stdin);
    freopen("out1b.txt","w",stdout);
    Int l = 0;
    int test;
    cin>>test;
    while(test--){
        l++;
        int arr[10] = {0};
        long long int n;
        cin>>n;
        if(n==0){
            pr(l);
            cout<<"INSOMNIA\n";
            continue;
        }
        long long int add = n;
        while(1){
            long long int temp = n;
            //cout<<temp<<"\n";
            while(temp!=0){
                long long int d = temp%10;
                if(arr[d]==0){
                    arr[d] = 1;
                }
                temp/=10;
            }
            int co = 0;
            for(int i=0;i<=9;i++){
                co+=arr[i];
            }
            if(co==10){
                break;
            }
            n+=add;
        }
        pr(l);
        cout<<n<<"\n";
    }
    return 0;
 }
