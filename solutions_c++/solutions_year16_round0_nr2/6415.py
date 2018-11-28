#include<bits/stdc++.h>

using namespace std;

string reduce(string S)
{
    string m="";
    char q=S[0];
    m+=S[0];
    for(int i=1;i<S.size();++i)
    {
        if(q!=S[i])
        {
            m+=S[i];
            q=S[i];
        }
    }
    return m;
}


int main()
{
    ofstream fs("nombre.txt");
    int T,acum;
    cin>>T;
    string S;
    for(int i=0;i<T;++i)
    {
        cin>>S;
        S=reduce(S);
        acum=0;
        char tmp=S[0];
        if(tmp=='-' && S.size()==1)
            acum=1;
        for(int j=1;j<S.size();++j)
        {
            if(S[j]!=tmp)
            {
                if(S[j]=='+')
                {
                    ++acum;
                }
                else
                {
                    acum+=2;
                }
                tmp='+';
            }
        }
        fs<<"Case #"<<i+1<<": "<<acum<<endl;
    }

    fs.close();
    return 0;
}
