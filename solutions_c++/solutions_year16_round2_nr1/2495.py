#include<stdio.h>
int main()
{
    int T,i,j,k,H[11];
    char s[3000];
    int ch[1000];
    scanf("%d", &T);
    for(i=0;i<T;i++)
    {
        int ch[1000];
        for(j=0;j<1000;j++)
        {
            ch[j]=0;
        }
        scanf("%s", &s);
        for(j=0;j<10;j++)
        {
            H[j]=0;
        }

        for(j=0;s[j]!='\0';j++)
        {
            ch[s[j]]++;
            if(s[j]=='Z')
            {
                H[0]++;
                ch['Z']--;
                ch['E']--;
                ch['R']--;
                ch['O']--;
            }
            if(s[j]=='W')
            {
                H[2]++;
                ch['T']--;
                ch['W']--;
                ch['O']--;
            }

            if(s[j]=='U')
            {
                H[4]++;
                ch['F']--;
                ch['O']--;
                ch['U']--;
                ch['R']--;
            }

            if(s[j]=='X')
            {
                H[6]++;
                ch['S']--;
                ch['I']--;
                ch['X']--;
            }

            if(s[j]=='G')
            {
                H[8]++;
                ch['E']--;
                ch['I']--;
                ch['G']--;
                ch['H']--;
                ch['T']--;
            }

        }
       // printf("O=%d\n", ch['O']);
        H[1]+=ch['O'];
        ch['N']-=ch['O'];
        ch['E']-=ch['O'];
        //ch['O']=0;


        H[3]+=ch['T'];
        ch['H']-=ch['T'];
        ch['R']-=ch['T'];
        ch['E']-=2*ch['T'];

        H[5]+=ch['F'];
        ch['I']-=ch['F'];
        ch['V']-=ch['F'];
        ch['E']-=ch['F'];

        H[7]+=ch['S'];
        ch['E']-=2*ch['S'];
        ch['V']-=ch['S'];
        ch['N']-=ch['S'];

        H[9]+=ch['I'];
        printf("Case #%d: ", i+1);
        for(j=0;j<10;j++)
        {
            if(H[j]>0)
           for(k=0;k<H[j];k++)
            {
                printf("%d", j);
            }
        }
        printf("\n");
    }

}
