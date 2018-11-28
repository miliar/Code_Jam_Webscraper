#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;
int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    std::ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    int ka=0;
    while(ka!=t){
        ka++;
        int a;
        int b,k;
        int count=0;
        cin>>a>>b>>k;
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
               if((i&j)<k)
                    count++;
            }
        }
        cout<<"Case #"<<ka<<": "<<count<<endl;
    }
}
