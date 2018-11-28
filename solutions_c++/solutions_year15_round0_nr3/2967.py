#include <iostream>
#include <string>

using namespace std;

const int i = 0, j = 1, k = 2, one = 3, negI = 4, negJ = 5, negK = 6, negOne = 7;

// i = 0, j = 1, k = 2, 1 = 3, -i = 4, -j = 5, -k = 6, -1 = 7

bool attempted[10005][3][8];

int mults[8][8];
int valToBeAbleToIncrease[3];

int convertToInt[128];


void setUpArrays()
{
    mults[i][one] = i;
    mults[i][i] = negOne;
    mults[i][j] = k;
    mults[i][k] = negJ;
    
    mults[negI][one] = negI;
    mults[negI][i] = one;
    mults[negI][j] = negK;
    mults[negI][k] = j;
    
    mults[j][one] = j;
    mults[j][i] = negK;
    mults[j][j] = negOne;
    mults[j][k] = i;
    
    mults[negJ][one] = negJ;
    mults[negJ][i] = k;
    mults[negJ][j] = one;
    mults[negJ][k] = negI;
    
    mults[k][one] = k;
    mults[k][i] = j;
    mults[k][j] = negI;
    mults[k][k] = negOne;
    
    mults[negK][one] = negJ;
    mults[negK][i] = negJ;
    mults[negK][j] = i;
    mults[negK][k] = one;
    
    mults[one][one] = one;
    mults[one][i] = i;
    mults[one][j] = j;
    mults[one][k] = k;
    
    mults[negOne][one] = negOne;
    mults[negOne][i] = negI;
    mults[negOne][j] = negJ;
    mults[negOne][k] = negK;
    
    valToBeAbleToIncrease[0] = i;
    valToBeAbleToIncrease[1] = j;
    valToBeAbleToIncrease[2] = k;
    
    convertToInt['i'] = i;
    convertToInt['j'] = j;
    convertToInt['k'] = k;
}

string str;

bool dp(int strPos, const int strSize, const int donePos, int createdPos, int currentVal)
{
    if (strPos == donePos && createdPos == 3)
        return true;
    else if (strPos == donePos)
        return false;
    else if (createdPos == 3)
        return false;
    else if (attempted[strPos][createdPos][currentVal])
        return false;
    
    attempted[strPos][createdPos][currentVal] = true;
    
    int current = convertToInt[str[strPos % strSize]];
    currentVal = mults[currentVal][current];
    
    if (currentVal == valToBeAbleToIncrease[createdPos])
        if (dp(strPos + 1, strSize, donePos, createdPos + 1, one))
            return true;
    
    return dp(strPos + 1, strSize, donePos, createdPos, currentVal);
}

int main()
{
    setUpArrays();
    
    int T;
    cin >> T;
    
    int size, sizeMult;
    
    for (int t = 1; t <= T; ++t)
    {
        cin >> size >> sizeMult >> str;
        int maxStrPos = size * sizeMult;
        
        // Need to clear attempted first
        for (int pos = 0; pos < maxStrPos; ++pos)
        {
            for (int createdPos = 0; createdPos < 3; ++createdPos)
            {
                for (int val = 0; val < 8; ++val)
                    attempted[pos][createdPos][val] = false;
            }
        }
        
        cout << "Case #" << t << ": " << (dp(0, str.size(), maxStrPos, 0, one) ? "YES\n" : "NO\n");
    }
}