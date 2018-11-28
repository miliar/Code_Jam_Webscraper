#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
int main()
{
    int T,r1,r2,i,j,mat1[4][4],mat2[4][4];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    for(int t=1;t<=T;t++){
        cin >> r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin >> mat1[i][j];
        cin >> r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin >> mat2[i][j];
        r1--;
        r2--;
        vector<int> common;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(mat1[r1][i]==mat2[r2][j]){
                    common.push_back(mat1[r1][i]);
                    break;
                }

            }
        }
        cout << "Case #" << t<<": ";
        if(common.size()==1)
            cout << common[0] << endl;
        else if (common.size()==0)
            cout << "Volunteer cheated!" << endl;
        else
            cout << "Bad magician!" << endl;
    }
    return 0;
}
