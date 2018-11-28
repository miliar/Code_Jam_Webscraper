#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

const int M[][5]=
{
    {0,  0,0,0,0},

    {0,  1,2,3,4},
    {0,  2,-1,4,-3},
    {0,  3,-4,-1,2},
    {0,  4,3,-2,-1}
};
int Tr[129];

int T,L,X,Len;
string InpString;
string S;
int FirstSplit,SecondSplit;

inline int Mult(int aa,int bb)
{
    int t=1;
    if (aa<0) {t=-1;aa=-aa;}
    if (bb<0) {t*=-1;bb=-bb;}
    return t*M[aa][bb];
}

int main()
{
    Tr['i']=2;
    Tr['j']=3;
    Tr['k']=4;

    cin >> T;
    for (int TestCase=1;TestCase<=T;TestCase++)
    {
        cin >> L >>X;
        cin >> InpString;

        S="";Len=L*X;
        while (X--) S+=InpString;

        //cout << "LYZ" <<S << endl;
        int now=1;
        //string::iterator FirstSplit;
        //string::iterator SecondSplit;

        for (int i=0;i<Len;i++)
        {
            now=Mult(now,Tr[S[i]]);
            if (now==2)
            {
                FirstSplit=i;
                break;
            }
            if (i==Len-1) FirstSplit=-1;
        }
        now=1;
        for (int i=Len-1;i>=0;i--)
        {
            now=Mult(Tr[S[i]],now);
            if (now==4)
            {
                SecondSplit=i;
                break;
            }
            if (i==0) SecondSplit=-1;
        }
        //cout << "FS " <<FirstSplit <<endl;
        //cout <<"SS "<<SecondSplit<<endl;
        now=1;
        for (int i=FirstSplit+1;i<SecondSplit;i++)
        {
            now=Mult(now,Tr[S[i]]);
        }
        if (FirstSplit!=-1 && SecondSplit!=-1 && now==3)
            printf("Case #%d: YES\n",TestCase);
        else printf("Case #%d: NO\n",TestCase);

    }



    return 0;
}
