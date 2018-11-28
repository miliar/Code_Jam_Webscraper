#include <iostream>
#include <stdio.h>
#include <math.h>
#define ll unsigned long long
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define sl(x) scanf("%llu",&x)
#define pl(x) printf("%llu\n",x)
#define min(x,y) ((x)<(y)?(x):(y))
using namespace std;

int main()
{
    int T,i,j,c;
    char mat[4][5],tmp[5];
    int flaga,flagb,blank,jd=0;
    si(T);
    c=0;
    while(T>0)
    {
        T--;
        c++;

        gets(tmp);

        for (i=0; i<4 ; i++ )
        {
            gets(mat[i]);

        }

        blank=0;  // rows
        for (i=0; i<4 ; i++ )
        {
            flaga=flagb=0;
            for (j=0; j<4 ; j++ )
            {
                switch(mat[i][j])
                {
                case 'X':
                    flaga++;
                    flagb=0;
                    break;
                case 'O':
                    flagb++;
                    flaga=0;
                    break;
                case 'T':
                    flaga++;
                    flagb++;
                    break;
                case '.':
                    blank++;
                    continue;
                }

            }
            //cout<<"falga="<<flaga<<" Flagb="<<flagb<<endl;
            if(flaga==4||flagb==4)
                break;

        }
        if(flaga==4)
        {
            cout<<"Case #"<<c<<": X won"<<endl;
            continue;
        }
        else if(flagb==4)
        {
            cout<<"Case #"<<c<<": O won"<<endl;
            continue;
        }
        //cols
        for (j=0; j<4 ; j++ )
        {
            flaga=flagb=0;
            for (i=0; i<4 ; i++ )
            {
                switch(mat[i][j])
                {
                case 'X':
                    flaga++;
                    flagb=0;
                    break;
                case 'O':
                    flagb++;
                    flaga=0;
                    break;
                case 'T':
                    flaga++;
                    flagb++;
                    break;
                case '.':
                    continue;
                    blank++;
                }
            }
            if(flaga==4||flagb==4)
                break;
        }
        if(flaga==4)
        {
            cout<<"Case #"<<c<<": X won"<<endl;
            continue;
        }
        else if(flagb==4)
        {
            cout<<"Case #"<<c<<": O won"<<endl;
            continue;
        }

        //diag
        flaga=flagb=0;
        for (i=0; i<4 ; i++ )
        {
            switch(mat[i][j])
            {
            case 'X':
                flaga++;
                flagb=0;
                break;
            case 'O':
                flagb++;
                flaga=0;
                break;
            case 'T':
                flaga++;
                flagb++;
                break;
            case '.':
                continue;
                blank++;
            }
        }
        //diag 2
        flaga=flagb=0;
        for (i=0; i<4 ; i++ )
        {
            switch(mat[i][4-1-i])
            {
            case 'X':
                flaga++;
                flagb=0;
                break;
            case 'O':
                flagb++;
                flaga=0;
                break;
            case 'T':
                flaga++;
                flagb++;
                break;
            case '.':
                continue;
                blank++;
            }
        }

        if(flaga==4)
        {
            cout<<"Case #"<<c<<": X won"<<endl;
            continue;
        }
        else if(flagb==4)
        {
            cout<<"Case #"<<c<<": O won"<<endl;
            continue;
        }


        if(blank>0)
            cout<<"Case #"<<c<<": Game has not completed"<<endl;
        else
            cout<<"Case #"<<c<<": Draw"<<endl;

    }


    return 0;
}

