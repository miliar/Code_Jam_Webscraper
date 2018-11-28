#include<iostream>
#include<fstream>
#include<set>
using namespace std;
int main()
{
    fstream fin("A-small-attempt0.in");
    fstream fout("A-small-attempt0.out");
    int TC,row,x;
    fin>>TC;
    int Counter=1;
    while(TC--)
    {
        fin>>row;
        set<int>S;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
        {
            fin>>x;
            if(i+1==row)
            {
                S.insert(x);
            }
        }
        fin>>row;
         int ct=0,ans=0;
         for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
        {
            fin>>x;
            if(i+1==row)
            {
                if(S.find(x)!=S.end())
                {
                    ct++;
                    ans=x;
                }
            }
        }
        fout<<"Case #"<<Counter++<<": ";
        if(ct==0)
            fout<<"Volunteer cheated!"<<endl;
        else if(ct==1)
            fout<<ans<<endl;
        else
            fout<<"Bad magician!"<<endl;
    }
    return 0;
}
