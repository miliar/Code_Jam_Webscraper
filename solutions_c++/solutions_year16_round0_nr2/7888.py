#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int i,count=0,len,t,c=0;
    string a;
    ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
    fin>>t;
    while(t>0)
    {
         c++;
         count=0;
         fin>>a;
         len=a.length();
         if(a[len-1]=='-')
             count++;
    
         for(i=len-2;i>=0;i--)
         {
             if((a[i]=='-' && a[i+1]=='+') || (a[i]=='+' && a[i+1]=='-'))
               count++;
         }
         fout<<"Case #"<<c<<": "<<count<<endl;
         t--;
    }
    return 0;
}
