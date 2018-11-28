#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <iomanip>


using namespace std;

#define INFY 10000000

int fr[17] = {0};
int mat[5][5];

int main() {
    freopen("/Users/arunamahesh/A-small-attempt0.in","r",stdin);
    freopen("/Users/arunamahesh/GCJ_output.txt","w",stdout);
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        for(int j = 1;j <= 16;j++) fr[j] = 0;
        int cr; cin>>cr;
        for(int j = 1; j <= 4;j++) {
            for(int k = 1;k <= 4;k++) cin>>mat[j][k];
        }
        for(int j = 1;j <= 4;j++) fr[mat[cr][j]]++;
        cin>>cr;
        for(int j = 1; j <= 4;j++) {
            for(int k = 1;k <= 4;k++) cin>>mat[j][k];
        }
        for(int j = 1;j <= 4;j++) fr[mat[cr][j]]++;
        int n2 = 0,n1 = 0;
        for(int j = 1;j <= 16;j++) {
            if(fr[j] == 1) n1++;
            if(fr[j] == 2) n2++;
        }
        if(n2 == 1) {
            int ans = 0;
            for(int j = 1;j <= 16;j++) {
                if(fr[j] == 2) {
                    ans = j;
                    break;
                }
            }
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
        else if(n2 > 1) {
            cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        }
        else {
            cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }
    }
}