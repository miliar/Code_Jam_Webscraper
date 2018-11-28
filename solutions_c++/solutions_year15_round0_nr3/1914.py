#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstring>
using namespace std;

/* 1 for 1, 2 for i, 3 for j, 4 for k, -2 for -i etc*/
int alRes[5][5] ={
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}
};


int alArry[10001];
static int cycIdx=0, idx=0;

int getChar(int cycNum, int num)
{
    
    for (;cycIdx<cycNum; cycIdx++) {
        if (idx<num)
            while (idx<num) {
                return alArry[idx++];
            }
        else {
            idx = 0;
        }
    }
    return 0;
}

int getRes(int alRes[5][5], int left, int right)
{
    int num = 0;
    if (left < 0) {
        left = -left;
        num++;
    }
    if (right < 0) {
        right = -right;
        num++;
    }
    if (num == 1) {
        return -alRes[left][right];
    } else {
        return alRes[left][right];
    }
}

int main(int argc, char *argv[])
{
    int i, j, k, t;

    long num, cycNum, res;
    int left, right, endFlag;
    char tch;

    if (argc < 2) {
        printf(" need file in,out ");
        return -1;
    }
    freopen(argv[1], "rt", stdin);
    freopen(argv[2], "wt", stdout);

    cin >> t;
    for (i = 0; i<t; i++) {
        cin >> num;
        cin >> cycNum;
        cycIdx=0;
        idx=0;
        memset(alArry, 0x00, sizeof(alArry));
        for (j = 0; j<num; j++) {
            cin >> tch;
            switch(tch) {
                case 'i':
                    alArry[j] = 2;
                    break;
                case 'j':
                    alArry[j] = 3;
                    break;
                case 'k':
                    alArry[j] = 4;
                    break;
            }
        }

        //get i
        res = 0;
        endFlag = 0;
        left = getChar(cycNum, num);
        res = left;
        while(res != 2) {    //get i
            right = getChar(cycNum, num);
            if (right==0) {
                endFlag= 1;
                break;
            }
            res = getRes(alRes, left, right);
            left = res;
        }
        if (res !=2 || endFlag) {
            cout << "Case #" << i+1 << ": NO" << endl;
            continue;
        }

        //get j
        left = getChar(cycNum, num);
        res = left;
        if (res == 0) {
            cout << "Case #" << i+1 << ": NO" << endl;
            continue;
        }
        while(res != 3) {
            right = getChar(cycNum, num);
            if (right==0) {
                endFlag= 1;
                break;
            }
            res = getRes(alRes, left, right);
            left = res;
        }
        if (res != 3 || endFlag) {
            cout << "Case #" << i+1 << ": NO" << endl;
            continue;
        }

        //get k
        left = getChar(cycNum, num);
        res = left;
        if (res == 0) {
            cout << "Case #" << i+1 << ": NO" << endl;
            continue;
        }
        while(res != 4 || cycIdx != cycNum || idx != num) {
            right = getChar(cycNum, num);
            if (right==0) {
                //endFlag= 1;
                break;
            }
            res = getRes(alRes, left, right);
            left = res;
        }
        if (res !=4 || endFlag) {
            cout << "Case #" << i+1 << ": NO" << endl;
            continue;
        }

        cout << "Case #" << i+1 << ": YES" << endl;
    }
}

