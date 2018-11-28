#include <iostream>
#include <cstdio>
#include<stack>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cctype>
#include <cmath>
#include <iomanip>
#include<cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;


//decietful war
//N identical blocks with masses [0,1] kg
//all blocks have different weights
//they play war with them
//each player knows the weight of their blocks
//naomi chooses a block, tells weight puts on scale
//then ken chooses a block, puts on scale
//heavier 1 gets a point and then both the blocks are destroyed

//naomi loses a lot, ken follows a single startegy everytime, naomi hates to lose
//deceitful war:
//naomi knows ken's blocks' weights
//naomi tells any num btw [0,1] not necessarily the block's weight
//must make sure that it isnt revealed chosen(naomi) != told(naomi)

int getWar(double naomi[],double ken[],int n,int start) {
    int j = 0;
    //normal war
    int busted = 0;
    for(int i = start;i < n;i++) {
        //cout<<naomi[i]<<" "<<ken[i]<<"\n";
        while(j < n && naomi[i] > ken[j-start]) {
            ++j;
        }
        if(j<n && naomi[i] < ken[j-start]){
            ++j;
            busted++;
        }
    }
    int war = n-start-busted;
    return war;
}

int main() {
    int t,n;
    int x = 0;
    freopen("/Users/shalini/Downloads/D.txt","r",stdin);
    freopen("/Users/shalini/Downloads/D1.txt", "w", stdout);
    cin>>t;
    while(t--) {
        ++x;
        cin>>n;
        double naomi[n],ken[n];
        for(int i = 0;i < n;i++) {
            cin>>naomi[i];
        }
        for(int i = 0;i < n;i++) {
            cin>>ken[i];
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int war = getWar(naomi,ken,n,0);
        int m = n;
        int i = 0;
        int j = n-1;
        int dwar = 0;
        while(m--) {
            bool fl = 1;
            for(int k = i;k < n;++k) {
                if(naomi[k] < ken[k-i]) {
                    fl = 0;
                    break;
                }
            }
            if(fl) {
                dwar = max(dwar,n-i);
                break;
            }
            if(naomi[i] < ken[j]) {
                i++;
                j--;
                dwar = max(dwar,getWar(naomi,ken,n,i));
            }
            else {
                break;
            }
        }
        cout<<"Case #"<<x<<": "<<dwar<<" "<<war<<"\n";
        
    }
    return 0;
}