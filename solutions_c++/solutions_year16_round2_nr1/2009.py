
#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("inputx11.in","r",stdin);
    freopen("resultout.txt","w",stdout);
    int t,it=1;
    cin>>t;
    while(t--)
    {
        string S;
        cin>>S;
        int A[26],B[10];
        for(int i=0;i<26;++i)
            A[i]=0;
        for(int i=0;i<10;++i)
            B[i]=0;
        int p=0;
        while(S[p])
        {
            ++A[S[p]-'A'];
            ++p;
        }
        B[6]=A['X'-'A'];
        A['S'-'A']-=A['X'-'A'];
        A['I'-'A']-=A['X'-'A'];
        A['X'-'A']-=A['X'-'A'];
        B[0]=A['Z'-'A'];
        A['E'-'A']-=A['Z'-'A'];
        A['R'-'A']-=A['Z'-'A'];
        A['O'-'A']-=A['Z'-'A'];
        A['Z'-'A']-=A['Z'-'A'];
        B[2]=A['W'-'A'];
        A['T'-'A']-=A['W'-'A'];
        A['O'-'A']-=A['W'-'A'];
        A['W'-'A']-=A['W'-'A'];
        B[8]=A['G'-'A'];
        A['E'-'A']-=A['G'-'A'];
        A['I'-'A']-=A['G'-'A'];
        A['H'-'A']-=A['G'-'A'];
        A['T'-'A']-=A['G'-'A'];
        A['G'-'A']-=A['G'-'A'];
        B[4]=A['U'-'A'];
        A['F'-'A']-=A['U'-'A'];
        A['O'-'A']-=A['U'-'A'];
        A['R'-'A']-=A['U'-'A'];
        A['U'-'A']-=A['U'-'A'];
        B[5]=A['F'-'A'];
        A['I'-'A']-=A['F'-'A'];
        A['V'-'A']-=A['F'-'A'];
        A['E'-'A']-=A['T'-'A'];
        A['F'-'A']-=A['F'-'A'];
        B[7]=A['S'-'A'];
        A['E'-'A']-=A['S'-'A'];
        A['V'-'A']-=A['S'-'A'];
        A['E'-'A']-=A['S'-'A'];
        A['N'-'A']-=A['S'-'A'];
        A['S'-'A']-=A['S'-'A'];
        B[1]=A['O'-'A'];
        A['N'-'A']-=A['O'-'A'];
        A['E'-'A']-=A['O'-'A'];
        A['O'-'A']-=A['O'-'A'];
        B[3]=A['T'-'A'];
        A['H'-'A']-=A['T'-'A'];
        A['R'-'A']-=A['T'-'A'];
        A['E'-'A']-=A['T'-'A'];
        A['E'-'A']-=A['T'-'A'];
        A['T'-'A']-=A['T'-'A'];
        B[9]=A['N'-'A']/2;
        A['I'-'A']-=(A['N'-'A']/2);
        A['E'-'A']-=(A['N'-'A']/2);
        A['N'-'A']-=A['N'-'A'];
        cout<<"Case #"<<it<<": ";
        ++it;
        for(int i=0;i<10;++i)
        {
            while(B[i]--)
            {
                printf("%c",'0'+i);
            }
        }
        printf("\n");
    }
    return 0;
}
