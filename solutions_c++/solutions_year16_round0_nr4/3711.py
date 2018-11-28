#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for (int c=1;c<=T;c++)
    {
        int K,C,S;
        long long int tile;
        scanf ("%d%d%d",&K,&C,&S);
        cout << "Case #" << c << ": ";
        if (K != S)
            cout << "LARGE";
        else
        {
        for (int i=0;i<S;i++)
        {
            tile = 1+i*pow(K,C-1);
            cout << tile << " ";
        }
        }
        cout << endl;
    }
    return 1;





}
