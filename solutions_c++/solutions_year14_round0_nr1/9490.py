#include <iostream>
#include<algorithm>
#include<set>
#include<cstring>
#include<fstream>

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int t,a,x;
set<int>s;
bool mark[20];

int main()
{
    fin>>t;
    for(int q=0;q<t;q++)
    {
        s.clear();
        memset(mark,false,sizeof mark);
        fin>>a;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                fin>>x;
                if(i==a-1)
                    mark[x]=true;
            }
        fin>>a;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                fin>>x;
                if(i==a-1 && mark[x])
                    s.insert(x);
            }
        fout<<"Case #"<<q+1<<": ";
        if(s.size()==0)
            fout<<"Volunteer cheated!"<<endl;
        else if(s.size()>1)
            fout<<"Bad magician!"<<endl;
        else
            fout<<*s.begin()<<endl;
    }
}
