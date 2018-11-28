#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,j;
    char fin[100],fout[100];
    cin>>fin>>fout;
    ofstream outfile;
    ifstream infile;
    outfile.open (fout);
    infile.open(fin);
    infile>>t;
    for(j=1; j<=t; j++)
    {
         string s;
        infile>>s;
        long long int count=0,i;
        for(i=0;i<s.size()-1;i++)
        {
            if(s[i]!=s[i+1])
                count++;
        }
        if(s[i]=='-')
            count++;
        outfile<<"Case #"<<j<<": "<<count<<endl;
    }
    outfile.close();
    infile.close();
    return 0;
}
