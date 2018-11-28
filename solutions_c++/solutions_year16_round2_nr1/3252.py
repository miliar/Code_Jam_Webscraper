#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=1;
    scanf("%d",&Test);
    while(Test--)
    {
        string S;
        cin>>S;
        int i;
        int A[10],C[27];
        for(i=0;i<10;i++)
            A[i]=0;
        for(i=0;i<27;i++)
            C[i]=0;
        for(i=0;i<S.length();i++)
        {
            C[S[i]-'A']++;
        }
        for(i=0;i<10;i++)
        {
            if(C['Z'-'A'])
            {
                A[0]=C['Z'-'A'];
                C['E'-'A']-=C['Z'-'A'];
                C['O'-'A']-=C['Z'-'A'];
                C['R'-'A']-=C['Z'-'A'];
                C['Z'-'A']-=C['Z'-'A'];
            }
            else if(C['G'-'A'])
            {
                A[8]=C['G'-'A'];
                C['E'-'A']-=C['G'-'A'];
                C['I'-'A']-=C['G'-'A'];
                C['H'-'A']-=C['G'-'A'];
                C['T'-'A']-=C['G'-'A'];
                C['G'-'A']-=C['G'-'A'];
            }
            else if(C['X'-'A'])
            {
                A[6]=C['X'-'A'];
                C['S'-'A']-=C['X'-'A'];
                C['I'-'A']-=C['X'-'A'];
                C['X'-'A']-=C['X'-'A'];
            }
            else if(C['U'-'A'])
            {
                A[4]=C['U'-'A'];
                C['F'-'A']-=C['U'-'A'];
                C['O'-'A']-=C['U'-'A'];
                C['R'-'A']-=C['U'-'A'];
                C['U'-'A']-=C['U'-'A'];
            }
            else if(C['F'-'A'])
            {
                A[5]=C['F'-'A'];
                C['I'-'A']-=C['F'-'A'];
                C['V'-'A']-=C['F'-'A'];
                C['E'-'A']-=C['F'-'A'];
                C['F'-'A']-=C['F'-'A'];
            }
            else if(C['S'-'A'])
            {
                A[7]=C['S'-'A'];
                C['E'-'A']-=2*C['S'-'A'];
                C['V'-'A']-=C['S'-'A'];
                C['N'-'A']-=C['S'-'A'];
                C['S'-'A']-=C['S'-'A'];
            }
            else if(C['I'-'A'])
            {
                A[9]=C['I'-'A'];
                C['N'-'A']-=2*C['I'-'A'];
                C['E'-'A']-=C['I'-'A'];
                C['I'-'A']-=C['I'-'A'];
            }
            else if(C['H'-'A'])
            {
                A[3]=C['H'-'A'];
                C['T'-'A']-=C['H'-'A'];
                C['R'-'A']-=C['H'-'A'];
                C['E'-'A']-=2*C['H'-'A'];
                C['H'-'A']-=C['H'-'A'];
            }
            else if(C['N'-'A'])
            {
                A[1]=C['N'-'A'];
                C['E'-'A']-=C['N'-'A'];
                C['O'-'A']-=C['N'-'A'];
                C['N'-'A']-=C['N'-'A'];
            }
            else if(C['T'-'A'])
            {
                A[2]=C['T'-'A'];
            }
            else
            {}
        }
        printf("Case #%d: ",k++);
        for(i=0;i<10;i++)
            if(A[i])
            {
                while(A[i])
                {
                    printf("%d",i);
                    A[i]--;
                }
            }
        printf("\n");
    }
    fclose(stdout);
    return 0;
}
