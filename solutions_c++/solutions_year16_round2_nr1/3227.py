#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
    int i,t,r=0;
    ofstream out("output.txt");
    ifstream in("input.in");

    in>>t;

    for (int k=0;k<t;k++)
    {
        string s1;
        int v[26]={0};
        in>>s1;
        for (i=0;i<s1.size();i++)
        {
            v[s1[i]-65]++;
        }
        int n=s1.size();
        int j=0;int f[2000]={0};
        while (n)
        {
            while(v[25]!=0)
            {
                v[25]--;v[4]--;v[17]--;v[14]--;
                n=n-4;
                f[j++]=0;

            }//zero

            while(v[22]!=0)
            {
                v[22]--;v[19]--;v[14]--;
                n=n-3;
                f[j++]=2;
            }//two

            while(v[20]!=0)
            {
                v[5]--;v[14]--;v[17]--;v[20]--;
                n=n-4;
                f[j++]=4;
            }//four

            while(v[23]!=0)
            {
                v[23]--;v[18]--;v[8]--;
                n=n-3;
                f[j++]=6;
            }//six

            while(v[6]!=0)
            {
                v[4]--;v[8]--;v[6]--;v[7]--;v[19]--;
                n=n-5;
                f[j++]=8;
            }//eight

            while(v[14]!=0)
            {
                v[14]--;v[13]--;v[4]--;;
                n=n-3;
                f[j++]=1;
            }//one

            while(v[19]!=0)
            {
                v[4]--;v[4]--;v[17]--;v[7]--;v[19]--;
                n=n-5;
                f[j++]=3;
            }//three

            while(v[5]!=0)
            {
                v[5]--;v[8]--;v[4]--;v[21]--;
                n=n-4;
                f[j++]=5;
            }//five

            while(v[18]!=0)
            {
                v[4]--;v[18]--;v[4]--;v[21]--;v[13]--;
                n=n-5;
                f[j++]=7;
            }//seven

            while(v[8]!=0)
            {
                v[4]--;v[8]--;v[13]--;v[13]--;
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
