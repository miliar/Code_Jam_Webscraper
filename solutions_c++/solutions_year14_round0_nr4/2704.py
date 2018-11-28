#include <functional>
#include <cstring>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    double Na[1001], Ke[1001];
    int N;
    //int arng1[4][4], arng2[4][4];
    //int chc1, chc2;
    //int i, j, cm, cmcnt;
    //double C, F, X, tots, pw;
    int i, j;
    freopen("DL.in", "r", stdin);
    freopen("DL.out", "w", stdout);
    cin>>T;
    int pickedn[1001];
    int pickedk[1001];
    int csno = 1;
    int totw, totd;
    while(T--)
    {
        //memset(Na, 0.0, sizeof(Na));
        //memset(Ke, 0.0, sizeof(Ke));
        memset(pickedn, 0, sizeof(pickedn));
        memset(pickedk, 0, sizeof(pickedk));
        cin>>N;
        totw = 0;
        totd = 0;
        for (i = 0; i < N; i++)
        {
            cin>>Na[i];

        }
        for (i = 0; i < N; i++)
        {
            cin>>Ke[i];
        }
        //sort Na and Ke
        sort(Na, Na + N);
        sort(Ke, Ke + N);
        //war
        bool cntrd = false;
        for (i = 0; i < N; i++)
        {
            cntrd = false;
            //try to counter Na[i] with Ke[j], if can't, break
            for (j = 0; j < N; j++)
            {
                if ((Ke[j] > Na[i]) && (pickedk[j] == 0))
                {
                    totd += 1;
                    pickedk[j] = 1;
                    cntrd = true;
                    break;
                }

            }
            if (cntrd == false)
                    break;
        }
        // opt war = (N - totd);
        //deceitful war
        for (i = (N - 1); i >= 0; i--)
        {
            cntrd = false;
            //try to counter Ke[i] with Na[j], if can't, pick the smallest one available
            for (j = 0; j < N; j++)
            {
                if ((Na[j] > Ke[i]) && (pickedn[j] == 0))
                {
                    totw += 1;
                    pickedn[j] = 1;
                    cntrd = true;
                    break;
                }
            }
            if (cntrd == false)
            {
                for (j = 0; j < N; j++)
                {
                    if (pickedn[j] == 0)
                    {
                        //pick it
                        pickedn[j] == 1;
                    }
                }
            }
        }
        //deceitful war = totw

        cout<<"Case #"<<csno<<": "<<totw<<" "<<(N - totd)<<endl;

        csno += 1;
    }
    return 0;
}
