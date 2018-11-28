#include <iostream>
#include <fstream>
using namespace std;

int m[8][8];



int main()
{
    m[0][0] = 0; m[0][1] = 1; m[0][2] = 2; m[0][3] = 3;
    m[0][4] = 4; m[0][5] = 5; m[0][6] = 6; m[0][7] = 7;

    m[1][0] = 1; m[1][1] = 4; m[1][2] = 3; m[1][3] = 6;
    m[1][4] = 5; m[1][5] = 0; m[1][6] = 7; m[1][7] = 2;

    m[2][0] = 2; m[2][1] = 7; m[2][2] = 4; m[2][3] = 1;
    m[2][4] = 6; m[2][5] = 3; m[2][6] = 0; m[2][7] = 5;

    m[3][0] = 3; m[3][1] = 2; m[3][2] = 5; m[3][3] = 4;
    m[3][4] = 7; m[3][5] = 6; m[3][6] = 1; m[3][7] = 0;

    m[4][0] = 4; m[4][1] = 5; m[4][2] = 6; m[4][3] = 7;
    m[4][4] = 0; m[4][5] = 1; m[4][6] = 2; m[4][7] = 3;

    m[5][0] = 5; m[5][1] = 0; m[5][2] = 7; m[5][3] = 2;
    m[5][4] = 1; m[5][5] = 4; m[5][6] = 3; m[5][7] = 6;

    m[6][0] = 6; m[6][1] = 3; m[6][2] = 0; m[6][3] = 5;
    m[6][4] = 2; m[6][5] = 7; m[6][6] = 4; m[6][7] = 1;

    m[7][0] = 7; m[7][1] = 6; m[7][2] = 1; m[7][3] = 0;
    m[7][4] = 3; m[7][5] = 2; m[7][6] = 5; m[7][7] = 4;

    int T,s1,s2,s3,x,l,index;
    bool f;
    string st,s;
    ifstream in;
    ofstream out;
    in.open("C-small-attempt1.in");
    out.open("out2.txt");
    in>>T;
    for(int t=1; t<=T; t++)
    {
        f = false;
        s1 = 0;
        s2 = 0;
        s3 = 0;
        index = 0;
        in>>l>>x;
        in>>st;
        s="";
        for(int i=0; i<x; i++)
        {
            s+=st;
        }
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='i')s[i]='1';
            else if(s[i]=='j')s[i]='2';
            else if(s[i]=='k')s[i]='3';
        }
        for(int i=0; i<s.size()&&!f; i++)
        {
            s1 = m[s1][s[i]-'0'];
        }
        index = 0;
        s1 = 0;
        while((s1 != 1 && s1 != 5)&&index<s.size())
        {
            s1 = m[s1][s[index]-'0'];
            index++;
        }
        if(s1 == 1)
        {
            s2 = 0;
        }
        else if(s1==5)
        {
            s2 = 4;
            s1 = 1;
        }
        while((s2 != 2 && s2 != 6)&&index<s.size())
        {
            s2 = m[s2][s[index]-'0'];
            index++;
        }
        if(s2 == 2)
        {
            s3 = 0;
        }
        else if(s2==6)
        {
            s3 = 4;
            s2 = 2;
        }
        while(index<s.size())
        {
            s3 = m[s3][s[index]-'0'];
            index++;
        }
        if(s1==1 && s2==2 && s3==3 && index==s.size())
        {
            f = true;
        }
        out<<"Case #"<<t<<": ";
        if(f)out<<"YES"<<endl;
        else out<<"NO"<<endl;
    }
    return 0;
}
