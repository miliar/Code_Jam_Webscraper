#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
    int i,t,r=0;
    cin>>t;

    for (int k=0;k<t;k++)
    {
        string myStr;
        int myArr[26]={0};
        cin>>myStr;
        for (i=0;i<myStr.size();i++)
        {
            myArr[myStr[i]-65]++;
        }
        int n=myStr.size();
        int j=0;int f[2000]={0};
        while (n)
        {
            while(myArr[25]!=0)
            {
                myArr[25]--;myArr[4]--;myArr[17]--;myArr[14]--;
                n=n-4;
                f[j++]=0;

            }//zero

            while(myArr[22]!=0)
            {
                myArr[22]--;myArr[19]--;myArr[14]--;
                n=n-3;
                f[j++]=2;
            }//two

            while(myArr[20]!=0)
            {
                myArr[5]--;myArr[14]--;myArr[17]--;myArr[20]--;
                n=n-4;
                f[j++]=4;
            }//four

            while(myArr[23]!=0)
            {
                myArr[23]--;myArr[18]--;myArr[8]--;
                n=n-3;
                f[j++]=6;
            }//six

            while(myArr[6]!=0)
            {
                myArr[4]--;myArr[8]--;myArr[6]--;myArr[7]--;myArr[19]--;
                n=n-5;
                f[j++]=8;
            }//eight

            while(myArr[14]!=0)
            {
                myArr[14]--;myArr[13]--;myArr[4]--;;
                n=n-3;
                f[j++]=1;
            }//one

            while(myArr[19]!=0)
            {
                myArr[4]--;myArr[4]--;myArr[17]--;myArr[7]--;myArr[19]--;
                n=n-5;
                f[j++]=3;
            }//three

            while(myArr[5]!=0)
            {
                myArr[5]--;myArr[8]--;myArr[4]--;myArr[21]--;
                n=n-4;
                f[j++]=5;
            }//fimyArre

            while(myArr[18]!=0)
            {
                myArr[4]--;myArr[18]--;myArr[4]--;myArr[21]--;myArr[13]--;
                n=n-5;
                f[j++]=7;
            }//semyArren

            while(myArr[8]!=0)
            {
                myArr[4]--;myArr[8]--;myArr[13]--;myArr[13]--;
                n=n-4;
                f[j++]=9;
            }//nine
        }
        sort (f,f+j);
        cout<<"Case #"<<k+1<<": ";
        for (i=0;i<j;i++)
        {
            cout<<f[i];
        }
        cout<<"\n";
    }
}
