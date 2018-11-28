#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <map>
#include <utility>
#include <fstream>
using namespace std;

#define mp make_pair
#define pb push_back
#define INF -1
#define MAX 10000007
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fi freopen("input.txt","r",stdin);
#define fo freopen("out.txt","w",stdout);
#define REP(i,n) for(int i=0;i<n;i++)
typedef pair<int,int> pii;

int main() {
    fi;
    fo;
    int t,a,b,k;
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        cin>>a>>b>>k;
        int cnt=0;
        for(int i=0;i<a;i++) {
            for(int j=0;j<b;j++) {
                //cout<<i<<"."<<j<<" "<<(i&j)<<"\n";
                if((i&j)<k) {
                    cnt++;
                }
            }
        }
        cout<<"Case #"<<cas<<": "<<cnt<<"\n";
    }
}
