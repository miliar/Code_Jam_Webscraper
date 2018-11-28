#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("i.in", "r", stdin);
    freopen("out.txt","w", stdout);
    int T, M, S[100], b;
    cin >> T;

    for(int i = 1; i <= T; i++)
    {
        cin >> M;
        for(int j = 0; j <= M; j++)
        {
            scanf("%1d", &S[j]);
        }
        int a = 0;
        int c = S[0];
        for(int k = 1; k <= M; k++)
        {
            if (k > c)
            {
                b = k - c;
                a = a + b;
                c = c + S[k] + b;

            }
            else{
                c = c + S[k];
            }
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    return 0;
}
