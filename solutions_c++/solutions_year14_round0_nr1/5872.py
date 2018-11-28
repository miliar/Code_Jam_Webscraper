#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>

#define SORT(x) sort(x.begin(),x.end())
#define REVERSE(x) reverse(x.begin(),x.end())
#define mp(x,y) make_pair(x,y)

using namespace std;

typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<VI> VII;

map<int,int > a1;
map<int,int > a2;

int main()
{
    ios_base::sync_with_stdio(false);

    freopen("small.in","r",stdin);
    freopen("outsmall.out","w",stdout);


    int T;
    cin>>T;
    int t=1;
    while(T--){

    a1.clear();
    a2.clear();

    int a,b;
    cin>>a;
    for(int k=0;k<4;k++){
        for(int i=0;i<4;i++){
            int num;cin>>num;
            a1[num]=k+1;
        }
    }
    cin>>b;
    for(int k=0;k<4;k++){
        for(int i=0;i<4;i++){
            int num;cin>>num;
            a2[num]=k+1;
        }
    }
    int c = 0,res=0;
    for(int k=1;k<=16;k++){
        if( a1[k]==a && a2[k]==b ){
            c++;
            res=k;
        }
    }

    cout<<"Case #"<<t<<": ";

    if(c==0)cout<<"Volunteer cheated!"<<endl;
    else if(c==1)cout<<res<<endl;
    else cout<<"Bad magician!"<<endl;

    t++;
    }

    return 0;
}
