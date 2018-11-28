#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("A1.in");//change input file name
    ofstream fout("output.txt");//change output file name
    int t;
    fin>>t;
    for(int j=0;j<t;j++)
    {
        string a,b;
        fin>>a;
        b[0]=='-1';
        for(int i=0;i<a.length();i++)
        {
            if(b[0]=='-1')
            {
                b[0]=a[0];
            }
            else if(b[0]<=a[i])
            {
                b.insert(b.begin(),a[i]);
            }
            else
            {
                b+=a[i];
            }
        }
        fout<<"Case #"<<j+1<<": "<<b<<endl;
    }
}
