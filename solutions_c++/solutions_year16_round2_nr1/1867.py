#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        string S;
        cin>>S;
        int X[26]={0,};
        for(i=0;i<S.length();i++)
        {
            X[S[i]-'A']++;
        }
        string Num[10]={"ZERO", "ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
        int sum=0;
        int Out[10]={0,};
        for(i=0;i<26;i++)sum+=X[i];
        while(X['Z'-'A']!=0)
        {
            Out[0]++;
            for(j=0;j<Num[0].length();j++)
            {
                X[Num[0][j]-'A']--;
            }
        }
        while(X['W'-'A']!=0)
        {
            Out[2]++;
            for(j=0;j<Num[2].length();j++)
            {
                X[Num[2][j]-'A']--;
            }
        }
        while(X['U'-'A']!=0)
        {
            Out[4]++;
            for(j=0;j<Num[4].length();j++)
            {
                X[Num[4][j]-'A']--;
            }
        }
        while(X['G'-'A']!=0)
        {
            Out[8]++;
            for(j=0;j<Num[8].length();j++)
            {
                X[Num[8][j]-'A']--;
            }
        }
        while(X['F'-'A']!=0)
        {
            Out[5]++;
            for(j=0;j<Num[5].length();j++)
            {
                X[Num[5][j]-'A']--;
            }
        }
        while(X['V'-'A']!=0)
        {
            Out[7]++;
            for(j=0;j<Num[7].length();j++)
            {
                X[Num[7][j]-'A']--;
            }
        }
        while(X['S'-'A']!=0)
        {
            Out[6]++;
            for(j=0;j<Num[6].length();j++)
            {
                X[Num[6][j]-'A']--;
            }
        }
        while(X['O'-'A']!=0)
        {
            Out[1]++;
            for(j=0;j<Num[1].length();j++)
            {
                X[Num[1][j]-'A']--;
            }
        }
        while(X['T'-'A']!=0)
        {
            Out[3]++;
            for(j=0;j<Num[3].length();j++)
            {
                X[Num[3][j]-'A']--;
            }
        }
        while(X['N'-'A']!=0)
        {
            Out[9]++;
            for(j=0;j<Num[9].length();j++)
            {
                X[Num[9][j]-'A']--;
            }
        }
        for(i=0;i<10;i++)
        {
            for(j=0;j<Out[i];j++)
            {
                printf("%d" , i);
            }
        }
        printf("\n");


    }

    return 0;
}
