#include <iostream>
#include <cstdio>
#include<fstream>
using namespace std;
int n, t, res;
int main()
{
    ifstream fin("r.txt");
    ofstream fout("w.txt");
    fin>>t;
    for(int i=0;i<t;i++)
    {
        string s;
        fin>>n;
        fin>>s;
        int sofar=0;
        res=0;
        for(int j=0;j<=n;j++)
        {
            if(sofar<j && s[j]!='0'){
                int val=j-sofar;
                res+=val, sofar+=val;
            }
            sofar+=s[j]-'0';
        }
        fout<<"case #"<<i+1<<": "<<res<<"\n";
    }

    return 0;
}
