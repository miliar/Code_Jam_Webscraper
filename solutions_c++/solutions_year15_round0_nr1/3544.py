#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 0; i < T; i++)
    {
        int up = 0;
        int Sol = 0;
        int Smax;
        cin>>Smax;
        string S;
        cin>>S;
        vector<int> V(Smax+1);
        for(int l = 0; l < Smax+1; l++)
        {
            V[l]=S[l];
            V[l] = V[l] - 48;
        }
        up = V[0];
        for(int k = 1; k < Smax+1; k++)
        {
            if(V[k]!=0)
            {
                if(up<k)
                {
                    Sol = Sol + k - up;
                    up = k;
                }
                up = up + V[k];
            }
        }
        cout<<"Case #"<<i+1<<": "<<Sol<<endl;
    }
    return 0;
}
