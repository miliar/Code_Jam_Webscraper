#include <iostream>
#include <string.h>
#include<fstream>
using namespace std;
int main()
{
    int t,n,i,j,k,ans;
    char s[100];
        ofstream outfile;
        ifstream infile;

        outfile.open("output.txt");
        infile.open("B-large.txt");
    infile>>t;
    for(i=1;i<=t;++i)
    {
    ans=0;
    infile>>s;
    n=strlen(s);
    if(s[n-1]=='-')
    k=1;
    else
    k=0;
    for(j=0;j<n-1;++j)
    if(s[j]!=s[j+1])
    ++ans;
    ans=ans+k;
    outfile<<"Case #"<<i<<": "<<ans<<endl;
    }

    infile.close();
    outfile.close();
    return 0;

}
