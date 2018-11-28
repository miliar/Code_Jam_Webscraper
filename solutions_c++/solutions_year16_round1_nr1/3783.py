#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <deque>
using namespace std;

bool bgr(int k, string& first, string& second)
{
    //assumes same length
    for(int i=0;i<k;i++)
    {
        if(first[i]>second[i])
            return true;
        if(first[i]<second[i])
            return false;
    }
    return true;
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("in.in");
    out.open("out.txt");
    int T;
    char * line;
    string S,A,A1,A2;
    in>>T;
    int t;
    for(t=1;t<=T;t++)
    {
        in>>S;
        //cout<<S<<endl;
        A=string();
        A1=string();
        A2=string();
        A.push_back(S[0]);
        for(int i=1;i<S.size();i++)
        {
            A1=A;
            A2=A;
            A1.push_back(S[i]);
            A2.insert(0,1,S[i]);
            if (bgr(i,A1,A2))
                A=A1;
            else
                A=A2;
        }
        out<<"Case #"<<t<<": ";
        for(int j=0;j<S.size();j++)
        {   out<<A[j];}
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
