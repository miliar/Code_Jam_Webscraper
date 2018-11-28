#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#pragma comment(linker, "/STACK:1000000000")
#pragma warning(disable : 4996)

using namespace std;

int m[1003];
int D[1003][1003];

int main()
{
    freopen("output.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    int T;
    cin >> T;
    for (int i = 1; i <= 1000; i++)
        for (int j = i+1; j <= 1000; ++j)
        {
            D[i][j] = j;
            for (int k = 1; k < j; ++k)
                D[i][j] = min(D[i][j], D[i][j - k] + D[i][k] + 1);
        }
    int n = 0;
    for (int i = 0; i < T; i++)
    {
        int res = 10000;
        cin >> n;
        for (int j = 0; j < n; j++)
            cin >> m[j];
        for (int j = 1; j <= 1000; j++)
        {
            int k = 0;
            for (int l = 0; l < n; l++)
                k = k + D[j][m[l]];
	    if(res > k+j)
		res = k+j;
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}