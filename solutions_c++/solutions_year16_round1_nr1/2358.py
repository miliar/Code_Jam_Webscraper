#include <bits/stdc++.h>
using namespace std;

ifstream f("wow.in");
ofstream g("wow.out");

#define LE 1066

bool viz[LE];

bool get_min(int left,int &right,string &str)
{
    if (right==-1) return false;

    int pos_min,min_val='A';

    for(int i=left;i<=right;++i)
          if (str[i]>=min_val)
          {
              min_val=str[i];
              pos_min=i;
          }

    right=pos_min-1;

    return true;
}

int pos;


int main()
{
    int nrt;
    f>>nrt;
    f.get();
    for (int tt=1;tt<=nrt;++tt)
    {
        string str;
        string result="";
        f>>str;
        int N=str.size();
        for(int i=0;i<=N;++i) viz[i]=false;

        pos=N-1;

        while (get_min(0,pos,str))
        {
            result+=str[pos+1];
            viz[pos+1]=true;
        }

        for(int i=0;i<N;++i)
             if (viz[i]==false)
                 result+=str[i];


        g<<"Case #"<<tt<<": "<<result<<'\n';
    }

    return 0;
}