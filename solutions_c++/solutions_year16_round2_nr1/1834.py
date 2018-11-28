/* بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
/* رَّبِّ زِدْنِى عِلْمًا */



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
#include <map>

using namespace std;

#define OUTPUT freopen("myfile.txt","w",stdout);
#define INPUT freopen("A-large (1).in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 100005
#define MOD 1000000009
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back

#define INF 1000000000



int main()
{
    //Bismillahir Rahmanir Rahim
    //Rabbi Zidni Ilma

    int T,tp=1;
    char inp[MAX];
    int i,len;
    int alpha[3000];
    int number[300];

    INPUT
    OUTPUT

    getInt(T)

    while(T--)
    {
        scanf("%s",inp);
        len=strlen(inp);

        for(i=0;i<300;i++)
        {
            alpha[i]=0;
        }

        for(i=0;i<10;i++)
        {
            number[i];
        }

        for(i=0;i<len;i++)
        {
            alpha[inp[i]]++;
        }

        number[6]=alpha['X'];
        alpha['S']-=number[6];
        alpha['I']-=number[6];
        alpha['X']-=number[6];

        number[8]=alpha['G'];
        alpha['E']-=number[8];
        alpha['I']-=number[8];
        alpha['G']-=number[8];
        alpha['H']-=number[8];
        alpha['T']-=number[8];

        number[7]=alpha['S'];
        alpha['S']-=number[7];
        alpha['E']-=number[7];
        alpha['V']-=number[7];
        alpha['E']-=number[7];
        alpha['N']-=number[7];

        number[2]=alpha['W'];
        alpha['T']-=number[2];
        alpha['W']-=number[2];
        alpha['O']-=number[2];

        number[3]=alpha['T'];
        alpha['T']-=number[3];
        alpha['H']-=number[3];
        alpha['R']-=number[3];
        alpha['E']-=number[3];
        alpha['E']-=number[3];

        number[4]=alpha['U'];
        alpha['F']-=number[4];
        alpha['O']-=number[4];
        alpha['U']-=number[4];
        alpha['R']-=number[4];

        number[5]=alpha['V'];
        alpha['F']-=number[5];
        alpha['I']-=number[5];
        alpha['V']-=number[5];
        alpha['E']-=number[5];

        number[0]=alpha['Z'];
        alpha['Z']-=number[0];
        alpha['E']-=number[0];
        alpha['R']-=number[0];
        alpha['O']-=number[0];

        number[1]=alpha['O'];
        alpha['O']-=number[1];
        alpha['N']-=number[1];
        alpha['E']-=number[1];

        number[9]=alpha['I'];




        printf("Case #%d: ",tp);

        //for (int i = 0; i < 10; ++i)
        {
          //  DEBUG(number[i])
        }

        for(i=0;i<10;i++)
        {
            while(number[i]--)
                printf("%d",i);
        }

        printf("\n");

        tp++;


    }


    return 0;
}

