#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//use true for +, false for -

int countflips(vector<bool>& seq)
{
    int res=0;
    int n=seq.size()-1;
    while(n>=0)
    {
        if(!seq[n])
            break;
        else
            n--;
    }
    if(n==-1)
        return 0;
    res=1;
    int cur=false;
    while(n>=0)
    {
        if(seq[n]!=cur)
        {
            res++;
            cur=seq[n];
            n--;
        }
        else
            n--;
    }
    return res;
}

void conv_string(string s,vector<bool>& state)
{
    int n=s.size();
    int i;
    state.clear();
    for(i=0;i<n;i++)
    {
        if(s[i]=='+')
            state.push_back(true);
        else
        {
            if(s[i]=='-')
                state.push_back(false);
        }
    }
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("in.in");
    out.open("out.txt");
    int T,t;
    string s;
    vector<bool> state;
    in>>T;
    for(t=1;t<=T;t++)
    {
        in>>s;
        conv_string(s,state);
        out<<"Case #"<<t<<": "<<countflips(state)<<endl;
    }
    in.close();
    out.close();

}
