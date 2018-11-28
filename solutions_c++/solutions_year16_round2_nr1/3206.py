#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
    int i,t,r=0;
    ofstream out("output.txt");
    ifstream in("input.txt");

    in>>t;

    for (int k=0;k<t;k++)
    {
        string s;
        int a[26]={0};
        in>>s;
        for (i=0;i<s.size();i++)
        {
            a[s[i]-65]++;
        }
        int n=s.size();
        int j=0;int f[2005]={0};
        while (n)
        {
            while(a[25]!=0)
            {
                a[25]--;a[4]--;a[17]--;a[14]--;
                n=n-4;
                f[j++]=0;

            }//zero

            while(a[22]!=0)
            {
                a[22]--;a[19]--;a[14]--;
                n=n-3;
                f[j++]=2;
            }//two

            while(a[20]!=0)
            {
                a[5]--;a[14]--;a[17]--;a[20]--;
                n=n-4;
                f[j++]=4;
            }//four

            while(a[23]!=0)
            {
                a[23]--;a[18]--;a[8]--;
                n=n-3;
                f[j++]=6;
            }//six

            while(a[6]!=0)
            {
                a[4]--;a[8]--;a[6]--;a[7]--;a[19]--;
                n=n-5;
                f[j++]=8;
            }//eight

            while(a[14]!=0)
            {
                a[14]--;a[13]--;a[4]--;;
                n=n-3;
                f[j++]=1;
            }//one

            while(a[19]!=0)
            {
                a[4]--;a[4]--;a[17]--;a[7]--;a[19]--;
                n=n-5;
                f[j++]=3;
            }//three

            while(a[5]!=0)
            {
                a[5]--;a[8]--;a[4]--;a[21]--;
                n=n-4;
                f[j++]=5;
            }//fiae

            while(a[18]!=0)
            {
                a[4]--;a[18]--;a[4]--;a[21]--;a[13]--;
                n=n-5;
                f[j++]=7;
            }//seaen

            while(a[8]!=0)
            {
                a[4]--;a[8]--;a[13]--;a[13]--;
                n=n-4;
                f[j++]=9;
            }//nine
        }
        sort (f,f+j);
        out<<"Case #"<<k+1<<": ";
        for (i=0;i<j;i++)
        {
            out<<f[i];
        }
        out<<"\n";
    }
}
