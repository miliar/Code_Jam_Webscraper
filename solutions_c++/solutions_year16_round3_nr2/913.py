#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>

using namespace std;

typedef unsigned long long ll;

int main() {
    freopen("/Users/shitian/Desktop/gcj/gcj/B-large.in", "r", stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/out.txt", "w", stdout);
    
    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        int ma[51][51];
        memset(ma,0,sizeof(ma));
        ll B;
        ll M;
        cin>>B>>M;
        if(pow(2,B-2)<M){
            cout<<"IMPOSSIBLE"<<endl;
        } else if(pow(2,B-2)==M){
            cout<<"POSSIBLE"<<endl;
            for(int i=0;i<B;i++){
                for(int j=0;j<B;j++){
                    if(j>i)cout<<1;
                    else cout<<0;
                }
                cout<<endl;
            }
        } else {
            cout<<"POSSIBLE"<<endl;
            
            ll x=M;
//            for(int i=0;i<B;i++){
//                ma[i][i+1]=1;
//            }
            bool fir=true;
            while(x){
                if(x==1){
                    ma[0][B-1]=1;
                    break;
                }
                ll t=1;
                ll in=0;
                while(x>=t){
                    t*=2;
                    in++;
                }
                t/=2;
                in-=1;
                in+=2;
                //cout<<"x: "<<x<<"  t: "<<t<<"  in: "<<in<<endl;
                if(t==0)t=1;
                ma[0][B-in]=1;
                if(fir){
                    for(int i=B-in;i<B;i++){
                        for(int j=i+1;j<B;j++){
                            ma[i][j]=1;
                        //    cout<<"i: "<<i<<" j: "<<j<<endl;;
                        }
                    }
                    fir=false;
                }
                x=x-t;
               // cout<<x<<" "<<t<<endl;
            }
            for(int i=0;i<B;i++){
                for(int j=0;j<B;j++){
                    cout<<ma[i][j];
                }
                cout<<endl;
            }
        }
    }
    return 0;
}