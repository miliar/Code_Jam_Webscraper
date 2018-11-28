#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstring>
using namespace std;

int alArry[1001];
long alLen;

int resArr[1001][1001];

long getMax(int arry[], int &idx)  //find the max num of arry
{
    long i, res;

    res = 0;
    for (i=0; i<alLen; i++) {
        if (res < arry[i]) {
            res = arry[i];
            idx=i;
        }
    }
    return res;
}

int main(int argc, char *argv[])
{
    int i, j, k;

    long t, num, cur, tmp, nextMax, eve, mineve, mink, res;
    int idx, alidx;
    long llevel;

    if (argc < 2) {
        printf(" need file in,out ");
        return -1;
    }
    freopen(argv[1], "rt", stdin);
    freopen(argv[2], "wt", stdout);

    cin >> t;
    for (i = 0; i<t; i++) {
        cin >> num;
        res = 0;
        alLen = 0;
        memset(alArry, 0x00, sizeof(alArry));
        for (j = 0; j<num; j++) {
            cin >> alArry[j];
        }
        alLen = num;

        //计算各个数字拆分的代价
        memset(resArr, 0x00, sizeof(resArr));
        for (j=0; j<num; j++) {
            cur = alArry[j];
            resArr[j][0] = cur;     //拆成1的代价
            for (k=1; k<cur-1; k++) {
                resArr[j][k] = cur/(k+1);       //拆成<=k+1的代价
                if (cur%(k+1) == 0) {
                    resArr[j][k]--;
                }
            }
        }
        //计算最小值
        eve = getMax(alArry, idx);
        res = eve;
        for (j=0; j<eve-1; j++) {
            tmp=0;
            for (k=0; k<num; k++) {
                tmp += resArr[k][j];
            }
            tmp += j+1;         //拆成<=j+1后，吃完的代价
            if (res > tmp) {
                res = tmp;
            }
        }
        
        cout << "Case #" << i+1 << ": " << res << endl;
    }
}


