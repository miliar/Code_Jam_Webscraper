#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

#define MAXX 1000000000
#define LL long long int

bool dig[10];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    int x = 0;
    while(t--){
        x++;
        LL n;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
        }
        else{
            LL temp;
            int flag = 0;
            LL z = 1;
            int ff = n;
            while(1){
                temp = n;
                while(temp != 0){
                    int k = temp%10;
                    //cout<<k<<" ";
                    dig[k] = true;
                    temp = temp/10;
                }
                for(int i = 0; i <= 9; i++){
                    if(dig[i] == false){
                        flag = 0;
                        break;
                    }else{
                        flag = 1;
                    }
                }
                if(flag == 1){
                    break;
                }
                z++;
                n = ff*z;
            }
            cout<<"Case #"<<x<<": "<<n<<"\n";
        }
        memset(dig, false, sizeof(dig));
    }
    return 0;
}
