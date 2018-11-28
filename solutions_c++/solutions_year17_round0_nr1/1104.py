#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <fstream>
using namespace std;
const int MAX = 1005;

int T,K;
char S[MAX];

void Flip(int pos)
{
    for (int i=pos;i<=pos+K-1;i++)
        S[i]=S[i]=='+'?'-':'+';
}

int main()
{
    /*ifstream fin("A-large.in");
    ofstream fout("Answer.out");
    cin.rdbuf(fin.rdbuf());
    cout.rdbuf(fout.rdbuf());*/
    cin>>T;
    for (int cases=1;cases<=T;cases++)
    {
        memset(S,0,sizeof(S));
        cin>>(S+1)>>K;
        int Ans=0;
        int len=strlen(S+1);
        for (int i=len-K+1;i>=1;i--)
            if (S[i+K-1]=='-')
                Flip(i),Ans++;
        bool flag=true;
        for (int i=1;i<=len;i++)
            if (S[i]=='-')
                flag=false;
        if (flag)
            cout<<"Case #"<<cases<<": "<<Ans<<endl;
        else
            cout<<"Case #"<<cases<<": "<<"IMPOSSIBLE"<<endl;

    }
    return 0;
}
