#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

void change(char *s,int n)
{
    for(int i=0;i<n;i++)
    {
        if(s[i]=='-')s[i]='+';
        else s[i]='-';
    }
}
int main()
{
    int n,t;
    ifstream infile; 
    infile.open("B-large.in",ios::in); 
    ofstream outfile;
    outfile.open("file1.dat", ios::out | ios::trunc );
    infile>>t;
    int c=1;
    while(t--)
    {
        char str[100];
        infile>>str;
        int x=0;
        int len=strlen(str);
        for(int i=len-1;i>=0;i--)
        {
            if(str[i]=='-') {change(str,i+1);x++;}
        }
        outfile<<"Case #"<<c++<<": "<<x<<endl;
    }
    return 0;
}
