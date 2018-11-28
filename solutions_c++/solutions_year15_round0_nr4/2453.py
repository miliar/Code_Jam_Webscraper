#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <cstdlib>
#include <string>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iterator>
#include <iomanip>
#include <limits.h>
#define debug(v) for(long long int i=0;i<v.size();++i)cout<<v[i]<<" ";cout<<endl;
using namespace std;
int main(){
	freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    long long int t;
    cin >> t;
    bool rc1[4][4];
    rc1[0][0] = true,rc1[0][1] = true,rc1[0][2] = true,rc1[0][3] = true;
    rc1[1][0] = true,rc1[1][1] = true,rc1[1][2] = true,rc1[1][3] = true;
    rc1[2][0] = true,rc1[2][1] = true,rc1[2][2] = true,rc1[2][3] = true;
    rc1[3][0] = true,rc1[3][1] = true,rc1[3][2] = true,rc1[3][3] = true;
    bool rc2[4][4];
    rc2[0][0] = false,rc2[0][1] = true,rc2[0][2] = false,rc2[0][3] = true;
    rc2[1][0] = true,rc2[1][1] = true,rc2[1][2] = true,rc2[1][3] = true;
    rc2[2][0] = false,rc2[2][1] = true,rc2[2][2] = false,rc2[2][3] = true;
    rc2[3][0] = true,rc2[3][1] = true,rc2[3][2] = true,rc2[3][3] = true;
    bool rc3[4][4];
    rc3[0][0] = false,rc3[0][1] = false,rc3[0][2] = false,rc3[0][3] = false;
    rc3[1][0] = false,rc3[1][1] = false,rc3[1][2] = true,rc3[1][3] = false;
    rc3[2][0] = false,rc3[2][1] = true,rc3[2][2] = true,rc3[2][3] = true;
    rc3[3][0] = false,rc3[3][1] = false,rc3[3][2] = true,rc3[3][3] = false;
    bool rc4[4][4];
    rc4[0][0] = false,rc4[0][1] = false,rc4[0][2] = false,rc4[0][3] = false;
    rc4[1][0] = false,rc4[1][1] = false,rc4[1][2] = false,rc4[1][3] = false;
    rc4[2][0] = false,rc4[2][1] = false,rc4[2][2] = false,rc4[2][3] = true;
    rc4[3][0] = false,rc4[3][1] = false,rc4[3][2] = true,rc4[3][3] = true;
    for(long long int q = 1; q <= t;++q){
        long long int x,r,c;
        cin >> x >> r >> c;
        r--,c--;
        switch(x){
        case 1:
            if(rc1[r][c])
                cout << "Case #" << q << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << q << ": " << "RICHARD" << endl;
            break;
        case 2:
            if(rc2[r][c])
                cout << "Case #" << q << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << q << ": " << "RICHARD" << endl;
            break;
        case 3:
            if(rc3[r][c])
                cout << "Case #" << q << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << q << ": " << "RICHARD" << endl;
            break;
        case 4:
            if(rc4[r][c])
                cout << "Case #" << q << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << q << ": " << "RICHARD" << endl;
            break;
        }
    }
   	return 0;
}
