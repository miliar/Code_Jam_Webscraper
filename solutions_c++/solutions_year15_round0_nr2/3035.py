#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;
int f[1002];
int n;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int numTest;
    int countTest;
    int res;
    cin >> numTest;
    int f[1002];
    for (countTest = 0; countTest < numTest; countTest++)
    {
        cin >> n;
        int num;
        int h;
        int upper = 0;
        int numCut;
        for (int i = 0; i < 1002; i++)
            f[i] = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> num;
            upper = max(upper, num);
            for (int j = 1; j <= num; j++)
            {
                /// tinh numCut
                    numCut = (num - j) / j;
                    if ((num - j) % j != 0) numCut++;
                ///
                if (f[j] == 0) f[j] = j + numCut;
                else f[j] = f[j] + numCut;
            }
        }
        res = 2000000000;
        for (int i = 1; i <= upper; i++)
            res = min(res, f[i]);

        cout << "Case #" << countTest + 1<<": " <<  res << endl;
    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
