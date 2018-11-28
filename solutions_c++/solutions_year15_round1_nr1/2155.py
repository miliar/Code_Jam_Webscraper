#include <iostream>

using namespace std;

main()
    {int t, T, N, m[10000], i, j, maior, resp1, resp2;

    cin>>T;

    for(t=1; t<=T; t++)
        {cin>>N;

        maior = -1;
        cin>>m[0];
        for(i=1; i<N; i++)
            {cin>>m[i];
            if(m[i-1]-m[i] > maior)
                maior = m[i-1]-m[i];}


            resp1 = 0;
            for(j=0; j<N-1; j++)
                {if(m[j] > m[j+1])
                resp1 += m[j]-m[j+1];}

            resp2=0;
            for(j=0; j<N-1; j++)
                {if(m[j] >= maior)
                resp2+=maior;
                else
                resp2+=m[j];}

            cout<<"Case #" << t << ": " << resp1 << ' ' <<resp2 << endl;}


    return 0;}
