#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <new>
#include <string>

using namespace std;

#define GETC getchar_unlocked()
inline void fastRead(int *a)
{
 register char c=0;
 int sign=1;
 while (c<33) c=GETC;
 *a=0;
 while (c>33)
 {
    if(c=='-'){sign=-1;}
    else{
     *a=*a*10+c-'0';
    }
     c=GETC;
 }
 *a = *a * sign;
}
 
#define S(__x__) fastRead(__x__)

typedef unsigned long long ULL;

#define N 100005
#define MOD 1000000009


int main() {
    //ios_base::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++) {
        int a[4][4],b[4][4];
        
        int fa,sa;
        cin>>fa;
        
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                cin>>a[i][j];
            }
        }
        cin>>sa;
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                cin>>b[i][j];
            }
        }
        int mc=0,mv=-1;fa--;sa--;
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                if(a[fa][i]==b[sa][j]) {
                    mc++;mv=a[fa][i];
                }
            }
        }
        if(mc==0)
            cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
        else if(mc>1)
            cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
        else 
            cout<<"Case #"<<k<<": "<<mv<<endl;
    }
    return 0;
}
