#include<bits/stdc++.h>
using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)

int main()
{
    int T, n;
    char c;
    scanf("%d ", &T);

    map<char, int> mapa;

    int quant[15]= {0};


    f(t, 1, T)
    {
        mapa.clear();
        f(i, 0, 9)
            quant[i]=0;

        for(; scanf("%c", &c)>0; )
        {
            if(c=='\n')
                break;
            mapa[c]++;
        }

        if(mapa.count('Z') )
        {
            n=quant[0]=mapa['Z'];

            if(mapa.count('Z'))
                mapa['Z']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
            if(mapa.count('R'))
                mapa['R']-=n;
            if(mapa.count('O'))
                mapa['O']-=n;
        }


        if(mapa.count('X') )
        {
            n=quant[6]=mapa['X'];

            if(mapa.count('S'))
                mapa['S']-=n;
            if(mapa.count('I'))
                mapa['I']-=n;
            if(mapa.count('X'))
                mapa['X']-=n;
        }

        if(mapa.count('W') )
        {
            n=quant[2]=mapa['W'];

            if(mapa.count('T'))
                mapa['T']-=n;
            if(mapa.count('W'))
                mapa['W']-=n;
            if(mapa.count('O'))
                mapa['O']-=n;
        }

        if(mapa.count('U') )
        {
            n=quant[4]=mapa['U'];

            if(mapa.count('F'))
                mapa['F']-=n;
            if(mapa.count('O'))
                mapa['O']-=n;
            if(mapa.count('U'))
                mapa['U']-=n;
            if(mapa.count('R'))
                mapa['R']-=n;
        }

        if(mapa.count('G') )
        {
            n=quant[8]=mapa['G'];

            if(mapa.count('E'))
                mapa['E']-=n;
            if(mapa.count('I'))
                mapa['I']-=n;
            if(mapa.count('G'))
                mapa['G']-=n;
            if(mapa.count('H'))
                mapa['H']-=n;
            if(mapa.count('T'))
                mapa['T']-=n;
        }

        if(mapa.count('T') )
        {
            n=quant[3]=mapa['T'];

            if(mapa.count('T'))
                mapa['T']-=n;
            if(mapa.count('H'))
                mapa['H']-=n;
            if(mapa.count('R'))
                mapa['R']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
        }

        if(mapa.count('F') )
        {
            n=quant[5]=mapa['F'];

            if(mapa.count('F'))
                mapa['F']-=n;
            if(mapa.count('I'))
                mapa['I']-=n;
            if(mapa.count('V'))
                mapa['V']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
        }

        if(mapa.count('I') )
        {
            n=quant[9]=mapa['I'];

            if(mapa.count('N'))
                mapa['N']-=n;
            if(mapa.count('I'))
                mapa['I']-=n;
            if(mapa.count('N'))
                mapa['N']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
        }


        if(mapa.count('O') )
        {
            n=quant[1]=mapa['O'];

            if(mapa.count('O'))
                mapa['O']-=n;
            if(mapa.count('N'))
                mapa['N']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
        }

        if(mapa.count('S') )
        {
            n=quant[7]=mapa['S'];

            if(mapa.count('S'))
                mapa['S']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
            if(mapa.count('V'))
                mapa['V']-=n;
            if(mapa.count('E'))
                mapa['E']-=n;
            if(mapa.count('N'))
                mapa['N']-=n;
        }
/*
        f(i, 0, 9)
        {
            cout<<"quant de "<<i<<" "<<quant[i]<<endl;
        }
        cout<<endl;*/

        cout<<"Case #"<<t<<": ";
        f(i, 0, 9)
        {
            f(j, 1, quant[i])
                cout<<i;

        }
        cout<<endl;

    }

    return 0;
}
