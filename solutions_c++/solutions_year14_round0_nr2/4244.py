#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<iomanip>

using namespace std;
#define getcx getchar_unlocked
#define scani(i) scanf("%d",&i)
#define scanl(i) scanf("%lld",&i)
#define LL long long
#define PB push_back
#define MP make_pair

int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        double ans=0,a=0,b=0,temp=0,C,F,X,rate=2;
        cin>>C>>F>>X;
        temp=X/rate;
        while(1){
            a=C/rate;
            b=X/(rate+F);
            if(temp>a+b){
                rate+=F;
                ans+=a;
                temp=b;
            }
            else{
                ans+=temp;
                break;
            }
        }
        cout<<setprecision(7)<<fixed;
        cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
    return 0;
}
