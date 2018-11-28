#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    #define int long long
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in",ios::in);
    fout.open("OutputL.in",ios::out);
    int t,i,n,Case=0,m,p,k;
    fin>>t;
    bool idx[10];

    while(Case<t)
    {
        for(i=0;i<10;i++)
        idx[i]=false;
        fin>>n;
        if(n==0)
            fout<<"Case #"<<Case+1<<":"<<" INSOMNIA"<<endl;
        else
        {
            m=n;
            i=1;
            while(i>0)
            {
                m=n*i;
                k=m;
                while(m>0)
                {
                    p=m%10;
                    m=m/10;
                    idx[p]=true;
                }
                i++;
                int c=0;
                for(int j=0;j<10;j++)
                {
                    if(idx[j]==true)
                        c++;
                }
                if(c==10)
                    break;
            }
            fout<<"Case #"<<Case+1<<": "<<k<<endl;
        }
        Case++;
    }
}
