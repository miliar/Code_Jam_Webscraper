#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("ans.txt");
    int t,j,len,count,i;
    char a[1001];
    //bool arr[11];
    fin>>t;
    //cout<<t;
    for(j=1;j<=t;j++)
    {
        fin>>a;
        fout<<"Case #"<<j<<": ";
        len=strlen(a);
        if(a[0]=='-') count=1;
        else count=0;
        for(i=0;i<len-1;i++)
        {
            if(a[i]=='+' && a[i+1]=='-') count+=2;
        }
        fout<<count<<endl;
    }
    return 0;
}
