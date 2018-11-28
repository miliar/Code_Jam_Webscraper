#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef unsigned long long ull;
short quat[5][5] = { {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}
};
int main() {
   freopen("/Users/vishnusankar/Desktop/CodeJam2015/input.in", "r", stdin);
   freopen("/Users/vishnusankar/Desktop/CodeJam2015/output", "w", stdout);
    vector<short> jValues,zValues;
    vector<short>charIntArr;
    int tc;
    scanf("%d", &tc);
    for (int t = 1;t <= tc;t++) {
        ull L = 0,X = 0;
        cin>>L>>X;
        string ijkStr;
        cin>>ijkStr;
        if((L == 1) || (L == 2 && X == 1)){
            printf("Case #%d: NO\n",t);
            continue;
        }
        short result = 0;
        bool storeJStart = false,storeZStart = false,prooved = false;
        for(ull l = 0;l < (L * X);l++) {
            short presnt = l % L;
            if(l < L){ // reading and cal result
                if(ijkStr[l] == 'i') charIntArr.push_back(2);
                else if(ijkStr[l] == 'j') charIntArr.push_back(3);
                else if(ijkStr[l] == 'k') charIntArr.push_back(4);
            }
            if(l == 0){
                result = charIntArr[presnt];
            }else{
                short mul1 = (result >= 0) ? 1:-1;
                short r = abs(result), c = charIntArr[presnt];
                result = (mul1) * quat[r][c];
            }
            
            for(int zv = 0; zv < zValues.size();zv++){
                short mul1 = (zValues[zv] >= 0) ? 1:-1;
                short r = abs(zValues[zv]), c = charIntArr[presnt];
                zValues[zv] = mul1 * quat[r][c];
                if(l + 1 == (L * X) && zValues[zv] == 4){
                    printf("Case #%d: YES\n",t);
                    prooved = true;
                    break;
                }
            }
            if(l + 1 == (L * X)){
                if(prooved)
                    break;
                else if(storeZStart && charIntArr[presnt] == 4){
                    printf("Case #%d: YES\n",t);
                    break;
                }
                printf("Case #%d: NO\n",t);
                break;
            }
            if(storeZStart){
                zValues.push_back(charIntArr[presnt]);
                storeZStart = false;
            }
            for(int jv = 0; jv < jValues.size();jv++){
                short mul1 = (jValues[jv] >= 0) ? 1:-1;
                short r = abs(jValues[jv]), c = charIntArr[presnt];
                jValues[jv] = mul1 * quat[r][c];
                if(jValues[jv] == 3)
                    storeZStart = true;
            }
            if(storeJStart){
                jValues.push_back(charIntArr[presnt]);
                storeJStart = false;
                if(charIntArr[presnt] == 3)
                    storeZStart = true;
            }
            if(result == 2)
                storeJStart = true;
        }
        charIntArr.clear();
        jValues.clear();zValues.clear();
    }
    return 0;
}
