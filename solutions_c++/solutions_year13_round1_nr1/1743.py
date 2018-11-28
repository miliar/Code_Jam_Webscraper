#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
#include<set>
#include<cmath>
using namespace std;
#define PB push_back
#define SL size()
#define LE length()
#define MP make_pair

int main(){
    int T; cin>>T;
    for(int kases = 1; kases <= T; kases++){
            long long r,t,res;
            cin>>r>>t;
            res = 0;
            while(t >= 0){
                    t-=(2*r+1); r+=2; res++;
            }if(t < 0) res--;
            cout<<"Case #"<<kases<<":";   cout<<" "<<res<<endl;//cout<<res<<" "<<r<<" "<<(res-r)/2<<endl;     
    }
}
