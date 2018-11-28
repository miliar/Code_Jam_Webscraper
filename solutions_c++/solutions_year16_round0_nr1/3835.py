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
using namespace std;
int main(){
    freopen("A-large.txt","r",stdin);
    freopen("outCG.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        int n;
        cin>>n;
        cout<<"Case #"<<tc<<": ";
        if(!n) cout<<"INSOMNIA\n";
        else{
            int tmp,arr[10]={0},c=1,ans=0;
            while(true){
                tmp=n*c;
                while(tmp){
                    if(arr[tmp%10]==0) ans++;
                    arr[tmp%10]=1;
                    tmp/=10;
                }
                if(ans==10) break;
                c++;
            }
            cout<<n*c<<endl;
        }
    }
}