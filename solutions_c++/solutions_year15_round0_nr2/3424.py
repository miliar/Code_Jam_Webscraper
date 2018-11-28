#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin>>T;
    for(int i = 0; i < T; i++)
    {
        int Max = -1;
        int Minlevel = -1;
        int P;
        cin>>P;
        vector<int> V(P);
        for(int k = 0; k < P; k++)
        {
            cin>>V[k];
            if (V[k] > Max)
                Max = V[k];
        }
        if(Max < 4)
            Minlevel = Max;
        else
        {
            for(int level = 1; level <= Max; level++)
            {
                int time = 0;
                for(int k = 0; k < P; k++)
                {
                    if(V[k]>level)
                    {
                        if((V[k]-level)%level == 0)
                        {
                            time = time + (V[k]-level)/level;
                        }
                        else
                        {
                            time = time + ((V[k]-level)/level)+1;
                        }
                    }
                }
                if(Minlevel == -1)
                    Minlevel = time+level;
                if (time+level < Minlevel)
                    Minlevel = time+level;
            }
        }
    cout<<"Case #"<<i+1<<": "<<Minlevel<<endl;
    }
    return 0;
}
