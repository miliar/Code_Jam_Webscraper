#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t=1,T,i,j,k,c;
    int mint,ans;
    string s;
    ifstream infile;
    infile.open("B-large.in");
    ofstream outfile;
    outfile.open("output.txt");
    infile>>T;
    while(T--)
    {
        infile>>s;
        int c=0,len,ans=0;
        len=s.size();
        for(i=0;i<len-1;i++)
        {
            if(s[i]!=s[i+1]) c++;
        }
        if(c==0)
        {
            if(s[0]=='+') ans=0;
            else ans=1;
            outfile<<"Case #"<<t++<<": "<<ans<<endl;
        }
        else
        {
            if(s[0]=='+')
            {
                if(c%2==0) ans=c;
                else ans=c+1;
            }
            else
            {
                if(c%2==0) ans=c+1;
                else ans=c;
            }
            outfile<<"Case #"<<t++<<": "<<ans<<endl;
        }
    }
    infile.close();
    outfile.close();
}
