#include<iostream>
#include<cmath>
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<string.h>
#include<ctime>
#include<map>
#include<assert.h>
using namespace std;
typedef long long ll;


int main(){

   // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;

    for(int p=1;p<=t;p++){
    int a,b,k;
    cin>>a>>b>>k;
    ll cnt=0;

    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            int res=i&j;
            if(res<k) cnt++;
        }
    }

    cout<<"Case #"<<p<<":"<<' '<<cnt<<endl;
    }
    return 0;


}
