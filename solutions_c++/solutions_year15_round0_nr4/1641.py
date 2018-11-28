#include <stdio.h>
#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cassert>
#include <sstream>
#include <iterator>

using namespace std;

#define file "file"
#define mp make_pair
#define pb push_back
#define xx real()
#define yy imag()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef complex<double> point;

void out(int t){
    if(t) printf("GABRIEL\n");
    else printf("RICHARD\n");
}

void solve(){
    int x,r,c;
    scanf("%d%d%d",&x,&r,&c);
    if(r == 1 || c == 1){
        if(x == 1) out(1);
        else{
            if((c % 2 == 0 || r % 2 == 0) && x == 2){
                out(1);
            }
            else out(0);
        }
        return;
    }
    if((r * c) % x != 0){
        out(0);
        return;
    }
    if(x == 1){
        out(1);
    }
    else if(x == 2){
        if((r * c) & 1) out(0);
        else out(1);
    }
    else if(x == 3){
        if(r < 3 && c < 3){
            out(0);
        }
        else{
            if(min(r,c) == 2){
                out(1);
            }
            else{
                out(1);
            }
        }
    }
    else if(x == 4){
        if(r < 4 && c < 4){
            out(0);
        }
        else{
            if(min(r,c) == 2) out(0);
            else if(min(r,c) == 3) out(1);
            else out(1);
        }
    }
    else{
        out(0);
    }
}

int main()
{
//	#ifndef ONLINE_JUDGE
//    assert(freopen("input.txt","r",stdin));
//    assert(freopen("output.txt","w",stdout));
//    #else
//    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
//    #endif
	int t = 1;
	int cs = 1;
	scanf("%d",&t);
	while(t--){
        printf("Case #%d: ",cs++);
		solve();
	}
	return 0;
}
