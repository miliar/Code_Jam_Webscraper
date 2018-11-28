#include <iostream>

#include <cstdio>

#include <cstdlib>

#include <cstring>

using namespace std;







int main()
{
    int i, t, k, j, head,l;

    int *a,*b;

    char maximum;
    char input[2001];
    //char *output[10] ={"ZERO", "ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);



    scanf("%d",&t);

    for(i =0; i <t; i++)
    {
        scanf("%s",input);

        a = (int *)calloc(26,sizeof(int));
        b = (int *)calloc(10,sizeof(int));

        l = strlen(input);

        for(j = 0; j < l; j++)
        {
            a[input[j] - 'A']++;
        }


        b[0] = a['Z'-'A'];
        a['Z'-'A'] -= b[0];
        a['E'-'A'] -= b[0];
        a['R'-'A'] -= b[0];
        a['O'-'A'] -= b[0];


        b[2] = a['W'-'A'];
        a['T'-'A'] -= b[2];
        a['W'-'A'] -= b[2];
        a['O'-'A'] -= b[2];


        b[4] = a['U'-'A'];
        a['F'-'A'] -= b[4];
        a['O'-'A'] -= b[4];
        a['U'-'A'] -= b[4];
        a['R'-'A'] -= b[4];

        b[6] = a['X'-'A'];
        a['S'-'A'] -= b[6];
        a['I'-'A'] -= b[6];
        a['X'-'A'] -= b[6];

        b[8] = a['G'-'A'];
        a['E'-'A'] -= b[8];
        a['I'-'A'] -= b[8];
        a['G'-'A'] -= b[8];
        a['H'-'A'] -= b[8];
        a['T'-'A'] -= b[8];

        b[1] = a['O'-'A'];
        a['O'-'A'] -= b[1];
        a['N'-'A'] -= b[1];
        a['E'-'A'] -= b[1];

        b[3] = a['R'-'A'];
        a['T'-'A'] -= b[3];
        a['H'-'A'] -= b[3];
        a['R'-'A'] -= b[3];
        a['E'-'A'] -= b[3];
        a['E'-'A'] -= b[3];

        b[5] = a['F'-'A'];
        a['F'-'A'] -= b[5];
        a['I'-'A'] -= b[5];
        a['V'-'A'] -= b[5];
        a['E'-'A'] -= b[5];

        b[7] = a['V'-'A'];
        a['S'-'A'] -= b[7];
        a['E'-'A'] -= b[7];
        a['V'-'A'] -= b[7];
        a['E'-'A'] -= b[7];
        a['N'-'A'] -= b[7];

        b[9] = a['I'-'A'];
        a['N'-'A'] -= b[9];
        a['I'-'A'] -= b[9];
        a['N'-'A'] -= b[9];
        a['E'-'A'] -= b[9];

        printf("Case #%d: ",i+1);

        for(j = 0; j < 10 ; j++)
        {
            for(k = 0; k < b[j];k++)
            {
                printf("%d",j);
            }
        }

        printf("\n");


    }

    return 0;

}
