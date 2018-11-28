#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <string.h>
#include <time.h>
#include <stack>
#include <set>
#include <queue>
#include <vector>
#include <list>
#define pb push_back
#define ll long long
#define mp make_pair
#define pll pair<long,long>
#define plll pair<long,long>
#define F first
#define S second
#define INF 1000000000


using namespace std;

bool w[10];

void pure(long a){
    while(a>0){
        w[a%10] = true;
        a/=10;
    }
}

int main()
{
    #ifdef LOCAL
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin.sync_with_stdio(0);
    cin.tie(0);
    long n,m;
    cin>>m;
    for(int k=0;k<m;k++){
    cin>>n;
    cout<<"Case #"<<k+1<<": ";
        bool gans=false;
        for(int i=0;i<10;i++) w[i]=false;
        for(int i=1;i<1000;i++){
            pure(i*n);
            bool flag = true;
            for(int j=0;j<10;j++){
                if(!w[j]) flag = false;
            }
            if(flag){
                cout<<i*n<<endl;
                gans = true;
                break;
            }
        }
        if(!gans) cout<<"INSOMNIA"<<endl;
}
    return 0;
}
