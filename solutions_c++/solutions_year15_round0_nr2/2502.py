#include <cmath>
#include <iostream>
using namespace std;

int compute(int *temp, int count)
{
    int max = 0;
    int maxi;
    for (int i = 0; i < count; i++)
        if (temp[i] > max) {
            max = temp[i];
            maxi = i;
        }
    if (max <= 3) {
        return max;
    } else {
        int *temptemp = new int[1000];
        for (int i = 0; i < count; i++)
            if (temp[i] > 1)
                temptemp[i] = temp[i]-1;
            else
                temptemp[i] = 0;
        int result1 = compute(temptemp, count) + 1;
        delete[] temptemp;
        
        int half = (sqrt(max)==floor(sqrt(max))?int(sqrt(max)):max/2);
        temp[maxi] -= half;
        temp[count++] = half;
        int result2 = compute(temp, count) + 1;
        
        return result1<result2?result1:result2;
    }
}

int main()
{
    int *temp = new int[1000];
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int count;
        cin >> count;
        for (int i = 0; i < count; i++)
            cin >> temp[i];
        
        int result = compute(temp, count);
        
        cout << "Case #" << t+1 << ": " << result << endl;
    }
    delete[] temp;
    return 0;
}
