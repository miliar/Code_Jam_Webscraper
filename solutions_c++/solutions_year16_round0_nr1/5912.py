#include <bits/stdc++.h>
using namespace std;
bool digits[10];
int main(){
    int t,flag=0;
    cin>>t;
    long long N,X,Y;
    for(int p=0;p<t;p++){
        cin>>N;
        flag=0;
        if(N==0){
            cout<<"Case #"<<p+1<<": INSOMNIA"<<endl;
            continue;
        }
        memset(digits,false,sizeof(digits));
        for(int i=1;flag==0;i++){
            X=i*N;
            Y=X;
            while(Y!=0){
                digits[Y%10]=true;
                Y/=10;
            }
            for(int g=0;digits[g];g++){
                if(g==9){
                    flag=1;
                    cout<<"Case #"<<p+1<<": "<<X<<endl;
                    break;
                }
            }
        }

    }
    return 0;
}
