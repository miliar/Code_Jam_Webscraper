#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define pb push_back

int ar[100][100];
int br[100][100];
int mx;
int r,c;
int findmaxforRow(int row){
    int ret = 0;
    for(int x=0;x<c;x++)
        ret = max(ret,ar[row][x]);
    return ret;
}

int findminforCol(int col){
    int ret = 101;
    for(int x=0;x<r;x++)
        if(ar[x][col]!=br[x][col])
            ret = min(ret,ar[x][col]);
    return ret;
}

void makerow(int row, int cut) {
    for(int x=0;x<c;x++)
        br[row][x] = min(cut,br[row][x]);
}

void makeCol(int col, int cut) {
    for(int x=0;x<r;x++)
        br[x][col] = min(cut,br[x][col]);
}

void cleanmem() {
    mx = 0;
    for(int x=0;x<100;x++)
        for(int y=0;y<100;y++)
            ar[x][y]=0;
}

int main()
{
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/ip.in","r",stdin);
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/anuj.out","w",stdout);
    int t;
    cin>>t;
    int cseno = 0;
    while(t--){
        cseno++;
        cin>>r>>c;
        cleanmem();
        for(int x =0 ; x< r;x++) {
            for(int y=0;y<c;y++){
                cin>>ar[x][y];
                mx = max(mx,ar[x][y]);
            }
        }
        for(int x =0 ; x< r;x++) {
            for(int y=0;y<c;y++){
                br[x][y]= mx;
            }
        }
        
        for(int x=0;x<r;x++){
            int k = findmaxforRow(x);
            makerow(x, k);
        }
        
        for(int y =0;y<c;y++){
            int k = findminforCol(y);
            makeCol(y, k);
        }
        int x;
        for(x=0;x<r;x++){
            for(int y=0;y<c;y++){
                if(ar[x][y]!=br[x][y]){
                    cout<<"Case #"<<cseno<<": NO\n";
                    x=200;y=c;
                }
            }
        }
        if(x!=201)
            cout<<"Case #"<<cseno<<": YES\n";
    }
    return 0;
}