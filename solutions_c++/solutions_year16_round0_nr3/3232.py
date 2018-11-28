#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <cmath>

using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>
#define MAXN 100000000

int prime[MAXN+1]={};

unsigned long long int tonsin(unsigned long long int n,int base,int N){
    unsigned long long int ni=1;
    unsigned long long int bi=1;
    unsigned long long int sum=0;

    for(;ni<(1<<N);){
        if(ni&n){
            sum+=bi;
        }
        ni<<=1;
        bi*=base;
    }
    return sum;
}

int ismayprime(unsigned long long int d){
    if(d<MAXN){
        if(prime[d]==-1){
            return 0;
        }
        else
        {
            return prime[d];
        }
    }
    else
    {
        if(d%2&&d%3&&d%5&&d%7&&d%11){
            return 0;
        }
        else{
            int a[]={2,3,5,7,11};
            rep(i,5){
                if(d%a[i]==0){
                    return a[i];
                }
            }
            return 0;
        }
    }
}

int main(){
    int M,N,J;
    cin>>M>>N>>J;

    unsigned long long int n=1;
    n<<=(N-1);
    n++;

    for(int i = 0; i < MAXN; i++){
        prime[i] = -1;
    }
    for(int i = 2; i < sqrt(MAXN); i++){
        if(prime[i]==-1){
            for(int j = 2 * i; j < MAXN; j += i){
                if(prime[j]==-1)prime[j] = i;
            }
        }
    }

    cout<<"Case #1:"<<endl;

    int cases=J;
    vector<int> ans;
    for(;n<(1<<N)&&cases!=0;n+=2){
        ans.clear();
        bool flag=true;
        for(int i=2;i<=10;i++){
            long long int d=tonsin(n,i,N);
            //cout<<n<<" "<<d<<endl;
            int div=ismayprime(d);
            if(!div){
                //cout<<d<<"is prime"<<endl;
                flag=false;
                break;
            }else{
                ans.push_back(div);
            }
        }
        if(flag){
            cout<<tonsin(n,10,N)<<" ";
            rep(i,8){
                cout<<ans[i]<<" ";
            }
            cout<<ans[8]<<endl;
            cases--;
        }
    }

    return 0;
}
