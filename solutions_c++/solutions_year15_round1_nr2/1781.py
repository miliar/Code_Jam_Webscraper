#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstring>
using namespace std;

long barberT[1001];
long barberCost[1001]; 
int  baberFlg[1001];
long bNum, nNum;

int getMin()
{
    int i, min;
    min = barberCost[0];
    for (i=1; i< bNum; i++) {
        if (min > barberCost[i]) {
            min = barberCost[i];
        }
    }
    return min;
}

int main(int argc, char *argv[])
{
    int i, j, k;
    long t, res;

    long maxBer;
    long maxNum;

    int lmin;

    if (argc < 2) {
        printf(" need file in,out ");
        return -1;
    }
    freopen(argv[1], "rt", stdin);
    freopen(argv[2], "wt", stdout);

    cin >> t;
    for (i = 0; i<t; i++) {
        cin >> bNum >> nNum;

        maxBer = 1;
        maxNum = 0;
        for (j = 0; j< bNum; j++) {
            cin >> barberT[j];
            maxBer *= barberT[j];
        }
        memcpy(barberCost, barberT, sizeof(barberT));
        memset(baberFlg, 0x00, sizeof(baberFlg));

        if (nNum <= bNum) {
            res = nNum;
            cout << "Case #" << i+1 << ": " << res << endl;
            continue;
        }
        
        maxNum = 0;
        for (j=0; j<bNum; j++) {
            maxNum += maxBer/barberT[j];
        }

        if (nNum >= maxNum) {
            nNum = nNum%maxNum;
            //k = 0;
        } 
        k = bNum;
        
        if (nNum == 0) {
            /*res = bNum;
            cout << "Case #" << i+1 << ": " << res << endl;
            continue;*/
            nNum = maxNum;
        }
        if (nNum <= bNum) {
            res = nNum;
            cout << "Case #" << i+1 << ": " << res << endl;
            continue;
        }
        cerr << "nNum=" << nNum << ",k=" << k <<endl;
        while(k < nNum) {
            // sub 1
            //lmin = getMin();
            for (j = 0; j< bNum; j++) {
                barberCost[j] --;
                if (barberCost[j] == 0) {
                    barberCost[j] = barberT[j];
                    k++;
                    if (k == nNum) {
                        res = j+1;
                        break;
                    }
                }
            }
        }

        cout << "Case #" << i+1 << ": " << res << endl;
    }
}


