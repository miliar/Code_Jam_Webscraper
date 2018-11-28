#include <iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("out1.txt");
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
       map<char,int> m1;
       m1['1']=0;
       m1['i']=1;
       m1['j']=2;
       m1['k']=3;
    int T1;
    in>>T1;
    string s;
    unsigned long tol,ktkt1;
    for(int i=1;i<=T1;i++)
    {

        char s1;
        int sin=1;
        int plas = 1;
        in>>tol>>ktkt1;
        in>>s;

        int er1 = 0;
        int k=0;
       while(k<ktkt1)
        {
            for(int j=0;j<s.size();j++)
            {
                s1=t[er1][m1[s[j]]];
                sin*=t1[er1][m1[s[j]]];
                if(m1[s1]== plas)
                {
                    plas++;
                    s1='1';
                }
                er1=m1[s1];
            }
            k++;
        }
        if(s1=='1' && sin==1 && plas == 4)
            out<<"Case #"<<i<<": YES"<<endl;
        else
            out<<"Case #"<<i<<": NO"<<endl;
       

    }


}
