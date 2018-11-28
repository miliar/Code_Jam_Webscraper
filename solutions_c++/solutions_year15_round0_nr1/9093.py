#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,smax;
    string p;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int fr =0;
        cin>>smax;
        cin>>p;
        int pcount =0;
        int pep=0;
        for(int j=0;j<smax+1;j++)
        {
            pep = (int)p.at(j) -48;
            if(j>pcount)
            {
                fr+=j-pcount;
                pcount+=(j-pcount);
            }
            pcount+=pep;
        }
        cout<<"case #"<<i+1<<":"<<" "<<fr<<endl;
    }
    return 0;
}
