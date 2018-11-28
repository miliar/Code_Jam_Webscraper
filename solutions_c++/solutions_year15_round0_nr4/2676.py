#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<fstream>
#include<sstream>

using namespace std;
int main()
{
    ifstream ifile;
    ofstream ofile;
    ifile.open("D-small-attempt0.in");
    ofile.open("outtt.txt");
    int tc;
    ifile>>tc;
    for(int i=0;i<tc;i++)
    {
        int x,r,c;
        string ans;
        ifile>>x>>r>>c;
        if(x==1)
            ans="GABRIEL";
        else if(x==2)
           {
            if((r*c)%x!=0)
               ans="RICHARD";
            else
                ans="GABRIEL";
            }
        else if(x==3)
            {
            if(r*c==x || (r*c)%x!=0)
               ans="RICHARD";
            else
                ans="GABRIEL";
            }
        else if(x==4)
            {
            if(r*c==8 || r*c==x || (r*c)%x!=0)
               ans="RICHARD";
            else
                ans="GABRIEL";
            }
        ofile<<"Case #"<<i+1<<": "<<ans<<endl;

    }
    return 0;
}
