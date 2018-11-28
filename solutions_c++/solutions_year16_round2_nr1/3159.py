#include <iostream>

using namespace std;

#include <stdio.h>
#include <stdlib.h>
int length(char str[])
{
    int c=0,i=0;
    while(str[i]!='\0')
    {
        c++;
        i++;
    }
    return c;
}
int main()
{
    freopen ("a.txt","r",stdin);
    freopen ("ao.txt","w",stdout);
    int test,i;
    scanf("%d",&test);
    for(i=0;i<test;i++)
    {
        int alpha[26]={0};
        int numb[10]={0};
        char str[2005];
        cin>>str;
        for(int j=0;j<length(str);j++)
        {
            alpha[str[j]-'A']++;
        }
        int q;
        if(alpha[25]>0)
        {
            q=alpha[25];
            for(int j=0;j<q;j++)
            {
                numb[0]++;
                alpha[25]--;
                alpha[4]--;
                alpha[17]--;
                alpha[14]--;
            }
        }
        if(alpha[22]>0)
        {
            q=alpha[22];
            for(int j=0;j<q;j++)
            {
                numb[2]++;
                alpha[19]--;
                alpha[22]--;
                alpha[14]--;
            }
        }
        if(alpha[20]>0)
        {
            q=alpha[20];
            for(int j=0;j<q;j++)
            {
                numb[4]++;
                alpha[20]--;
                alpha[5]--;
                alpha[14]--;
                alpha[17]--;
            }
        }
//        for(int j=0;j<26;j++)
//        {
//            //for(int k=0;k<numb[j];k++)
//            //{
//                cout<<alpha[j];
//            //}
//        }
        if(alpha[23]>0)
        {
            q=alpha[23];
            for(int j=0;j<q;j++)
            {
                numb[6]++;
                alpha[23]--;
                alpha[18]--;
                alpha[8]--;

            }
        }
        if(alpha[6]>0)
        {
            q=alpha[6];
            for(int j=0;j<q;j++)
            {
                numb[8]++;
                alpha[6]--;
                alpha[4]--;
                alpha[8]--;
                alpha[7]--;
                alpha[19]--;
            }
        }
        if(alpha[5]>0)
            {
            q=alpha[5];

            for(int j=0;j<q;j++)
            {
                numb[5]++;
                alpha[5]--;
                alpha[8]--;
                alpha[21]--;
                alpha[4]--;

            }
            }


            if(alpha[18]>0)
            {
            q=alpha[18];

            for(int j=0;j<q;j++)
            {
                numb[7]++;
                alpha[18]--;
                alpha[4]--;
                alpha[21]--;
                alpha[4]--;
                alpha[13]--;
            }
            }
        if(alpha[14]>0)
        {
            q=alpha[14];
            for(int j=0;j<q;j++)
            {
                numb[1]++;
                alpha[14]--;
                alpha[13]--;
                alpha[4]--;
            }
        }
        if(alpha[8]>0)
        {
            q=alpha[8];
            for(int j=0;j<q;j++)
            {
                numb[9]++;
                alpha[13]--;
                alpha[13]--;
                alpha[8]--;
                alpha[4]--;
            }
        }
        if(alpha[17]>0)
        {
            q=alpha[17];
            for(int j=0;j<q;j++)
            {
                numb[3]++;
                alpha[19]--;
                alpha[7]--;
                alpha[17]--;
                alpha[4]--;
                alpha[4]--;
            }
        }

        printf("Case #%d: ",i+1);
        for(int j=0;j<10;j++)
        {
            for(int k=0;k<numb[j];k++)
            {
                cout<<j;
            }
        }
        printf("\n");
    }
    return 0;
}
