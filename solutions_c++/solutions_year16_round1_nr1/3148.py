#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream fp;
    fp.open("A-large.in",ios::in);
    ofstream fo;
    fo.open("out.txt",ios::out);
    int t;
    int i,m,j,n,flag,l;
    string s;
    char k[2000]={0};
    fp>>t;
    for(l=1;l<=t;l++)
    {

        fp>>s;
        k[1000]=s[0];
        m=1000;
        j=1001;
        for(i=1;i<s.length();i++)
        {
            if(s[i]>=k[m])
            {
                k[--m]=s[i];
            }
            else
            {
                k[j++]=s[i];
            }
        }
        //fo<<"Case #"<<i<<": "<<l<<endl;
        fo<<"Case #"<<l<<": ";
        for(i=m;i<j;i++)
            fo<<k[i];

        fo<<endl;
    }

}
