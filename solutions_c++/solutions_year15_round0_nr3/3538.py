#include <iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

main()
{
    ifstream in("C-small-attempt3.in");
    ofstream out("out.txt");
     char t[4][4];
     int t1[4][4];
    t[0][0]='1';
    t[0][1]='i';
    t[0][2]='j';
    t[0][3]='k';
    t[1][0]='i';
    t[1][1]='1';
    t[1][2]='k';
    t[1][3]='j';
    t[2][0]='j';
    t[2][1]='k';
    t[2][2]='1';
    t[2][3]='i';
    t[3][0]='k';
    t[3][1]='j';
    t[3][2]='i';
    t[3][3]='1';

    t1[0][0]=1;
    t1[0][1]=1;
    t1[0][2]=1;
    t1[0][3]=1;
    t1[1][0]=1;
    t1[1][1]=-1;
    t1[1][2]=1;
    t1[1][3]=-1;
    t1[2][0]=1;
    t1[2][1]=-1;
    t1[2][2]=-1;
    t1[2][3]=1;
    t1[3][0]=1;
    t1[3][1]=1;
    t1[3][2]=-1;
    t1[3][3]=-1;
       map<char,int> g;
       g['1']=0;
       g['i']=1;
       g['j']=2;
       g['k']=3;
    int test;
    in>>test;
    string s;
    long long tol,tkrar;
    for(int i=1;i<=test;i++)
    {

        char ci;
        int sin=1;
        int plas = 1;
        in>>tol>>tkrar;
        in>>s;

        int rr = 0;
        for(int k=0;k<tkrar;k++)
        {
            for(int j=0;j<s.size();j++)
            {
                ci=t[rr][g[s[j]]];
                sin*=t1[rr][g[s[j]]];
                if(g[ci]== plas)
                {
                    plas++;
                    ci='1';
                }
                rr=g[ci];
            }
        }
        if(ci=='1' && sin==1 && plas == 4)
            out<<"Case #"<<i<<": YES"<<endl;
        else
            out<<"Case #"<<i<<": NO"<<endl;
        /*
        if(tkrar%2 && g[ci]==0 && sin==-1)
            out<<"Case #"<<i<<": "<<"YES"<<endl;

        if(tkrar%2 && g[ci]==0 && sin==1)
            out<<"Case #"<<i<<": "<<"NO"<<endl;

        if(!(tkrar%2) && g[ci]==0 )
            out<<"Case #"<<i<<": "<<"NO"<<endl;

        if(!(tkrar%2) && g[ci]!=0)
            if((tkrar/2)%2 && (tkrar/2)>2)
                out<<"Case #"<<i<<": "<<"YES"<<endl;
            else
                out<<"Case #"<<i<<": "<<"NO"<<endl;

        if((tkrar%2) && g[ci]!=0)
            out<<"Case #"<<i<<": "<<"NO"<<endl;
*/

    }


}
