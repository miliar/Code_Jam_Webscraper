#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <stdio.h>
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;  // H A M L E T
long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}long long lcm(long long a,long long b){return a*(b/gcd(a,b));}

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    
    int tc;
    cin>>tc;
    
    
    for(int caso=1;caso<=tc;caso++){
        cout<<"Case #"<<caso<<": ";
        int c[11];
        int a[11];
        int n;    
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>c[i];
            a[i]=c[i];
        }
        
        sort(a,a+n);
        int dev=1<<24;
        do{
            int a2[n];
            
            for(int i=0;i<n;i++){
                a2[i]=a[i];    
            }
            //    cout<<a[i]<<" ";
            //cout<<endl;
            
            bool ok=1;
            
            bool aumenta=1;
            for(int i=1;i<n;i++){
                if(a[i]>a[i-1]){
                    if(aumenta){
                        continue;    
                    }else{
                        ok=0;
                        break;    
                    }
                }else{
                    if(aumenta){
                        aumenta=0;    
                    }else{
                        continue;    
                    }    
                }
                
            }
            
            
            if(ok==0)continue;
            
            int cont=0;
            for(int i=0;i<n;i++){
                if(a2[i]!=c[i]){
                    for(int j=i+1;j<n;j++){
                        if(a2[j]==c[i]){
                            for(int k=j-1;k>=i;k--){
                                swap(a2[k],a2[k+1]);    
                                cont++;
                            }
                            break;
                        }    
                    }    
                }    
            }
            dev=min(dev,cont);
        }while(next_permutation(a,a+n));
        
        cout<<dev<<endl;
    }
    
    
    return 0;
}
