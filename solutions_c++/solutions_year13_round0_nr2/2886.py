#include <iostream>
#include <cstring>
using namespace std;
int n, N, w, h;
int x[10001];
int maxH[101], maxV[101];

int main()
{
    int i;
    cin >> N;
    for (n = 1; n <= N; n++)
    {
        memset(maxH, 0, sizeof(maxH));
        memset(maxV, 0, sizeof(maxV));
        cin >> h >> w;
        for (i = 0; i < w * h; i++)
        {
            cin >> x[i];
            maxH[i / w] = max(maxH[i / w], x[i]);
            maxV[i % w] = max(maxV[i % w], x[i]);
        }
        for (i = 0; i < w * h; i++)
        {
            //            cerr << i << " (" << (int)(i / w) << ", " << (i % w) << "): " << x[i] << " [" << maxH[i / w] << ", " << maxV[i % w] << "]" << endl;
            if (x[i] < maxH[i / w] && x[i] < maxV[i % w]) break;
        }
        cout << "Case #" << n << ": " << (i == w * h ? "YES" : "NO") << endl;
    }
}
