#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int cc(string &,int,int);
int main()
{
    ifstream cin; cin.open("input.txt");
    ofstream cout; cout.open("output.txt");
    int t,n;
    string in;
    cin>>t;
    int res;
    for(int i=0;i<t;i++)
    {
        cin>>in;
        cin>>n;
        res=0;
        int l=in.length();
        for(int j=0;j<l;j++)
        {
            res+=cc(in,j,n);
            //cout <<res<<' ';
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    return 0;
}

int cc(string &str,int s,int n)
{
    int res=0;
    int num=0;
    int l=str.length();
    for(int i=s;i<l;i++)
    {
        if((str[i]=='a')||(str[i]=='e')||(str[i]=='o')||(str[i]=='i')||(str[i]=='u')) {num=0; continue;}
        num++;
        if(num==n) return l-i;
    }
    return res;
}
