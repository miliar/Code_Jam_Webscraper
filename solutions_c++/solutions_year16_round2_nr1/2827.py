#include<cstdio>

using namespace std;


char str[2010];
int hist[30];
int ans[10];

int main(void)
{
    int cases,cas;
    scanf("%d",&cases);

    for(cas=1;cas<=cases;cas++){
        for(int i=0;i<30;i++){
            hist[i] =0;
        }

        for(int i=0;i<10;i++){
            ans[i] = 0;
        }

        scanf("%s",str);
        for(int i=0;str[i];i++){
            hist[str[i]-'A']++;
        }


        printf("Case #%d: ",cas);

        int n = 0;
        //zero
        if(hist['Z'-'A']>0){
            n = hist['Z'-'A'];

            hist['Z'-'A'] -= n;
            hist['E'-'A'] -= n;
            hist['R'-'A'] -= n;
            hist['O'-'A'] -= n;

            ans[0]+=n;
        }

        //six
        if(hist['X'-'A']>0){
            n = hist['X'-'A'];

            hist['S'-'A'] -= n;
            hist['I'-'A'] -= n;
            hist['X'-'A'] -= n;

            ans[6] +=n;
        }

        //seven
        if(hist['S'-'A']>0){
            n = hist['S'-'A'];

            hist['S'-'A'] -= n;
            hist['E'-'A'] -= n;
            hist['V'-'A'] -= n;
            hist['E'-'A'] -= n;
            hist['N'-'A'] -= n;

            ans[7] +=n;
        }

        //FIVE
        if(hist['V'-'A']>0){
            n = hist['V'-'A'];

            hist['F'-'A'] -= n;
            hist['I'-'A'] -= n;
            hist['V'-'A'] -= n;
            hist['E'-'A'] -= n;

            ans[5] +=n;
        }

        //FOUR
        if(hist['F'-'A']>0){
            n = hist['F'-'A'];

            hist['F'-'A'] -= n;
            hist['O'-'A'] -= n;
            hist['U'-'A'] -= n;
            hist['R'-'A'] -= n;

            ans[4] +=n;
        }

        //THREE
        if(hist['R'-'A']>0){
            n = hist['R'-'A'];

            hist['T'-'A'] -= n;
            hist['H'-'A'] -= n;
            hist['R'-'A'] -= n;
            hist['E'-'A'] -= n;
            hist['E'-'A'] -= n;

            ans[3] +=n;
        }

        //TWO
         if(hist['W'-'A']>0){
            n = hist['W'-'A'];

            hist['T'-'A'] -= n;
            hist['W'-'A'] -= n;
            hist['O'-'A'] -= n;

            ans[2] +=n;
        }

        //ONE
        if(hist['O'-'A']>0){
            n = hist['O'-'A'];

            hist['O'-'A'] -= n;
            hist['N'-'A'] -= n;
            hist['E'-'A'] -= n;

            ans[1] +=n;
        }

        //EIGHT
         if(hist['T'-'A']>0){
            n = hist['T'-'A'];

            hist['I'-'A'] -= n;




            ans[8] +=n;
        }

        //NINE
        if(hist['I'-'A']>0){
            n = hist['I'-'A'];
            ans[9] +=n;
        }

        for(int i=0;i<=9;i++){
            for(int j=0;j<ans[i];j++)
                putchar(i+'0');
        }
        putchar('\n');
    }

    return 0;
}
