#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
    int i,t;
    ofstream outFile("output.txt");
    ifstream inFile("input.txt");

    inFile>>t;

    for (int k=0;k<t;k++)
    {
        string strInput;
        int vCount[26]={0};
        inFile>>strInput;
        for (i=0;i<strInput.size();i++)
        {
            vCount[strInput[i]-65]++;
        }
        int n=strInput.size();
        int j=0;
        int fil[2000]={0};
        while (n)
        {
            while(vCount[25]!=0)
            {
                vCount[25]--;vCount[4]--;vCount[17]--;vCount[14]--;
                n=n-4;
                fil[j++]=0;

            }

            while(vCount[22]!=0)
            {
                vCount[22]--;vCount[19]--;vCount[14]--;
                n=n-3;
                fil[j++]=2;
            }

            while(vCount[20]!=0)
            {
                vCount[5]--;vCount[14]--;vCount[17]--;vCount[20]--;
                n=n-4;
                fil[j++]=4;
            }

            while(vCount[23]!=0)
            {
                vCount[23]--;vCount[18]--;vCount[8]--;
                n=n-3;
                fil[j++]=6;
            }

            while(vCount[6]!=0)
            {
                vCount[4]--;vCount[8]--;vCount[6]--;vCount[7]--;vCount[19]--;
                n=n-5;
                fil[j++]=8;
            }

            while(vCount[14]!=0)
            {
                vCount[14]--;vCount[13]--;vCount[4]--;;
                n=n-3;
                fil[j++]=1;
            }

            while(vCount[19]!=0)
            {
                vCount[4]--;vCount[4]--;vCount[17]--;vCount[7]--;vCount[19]--;
                n=n-5;
                fil[j++]=3;
            }

            while(vCount[5]!=0)
            {
                vCount[5]--;vCount[8]--;vCount[4]--;vCount[21]--;
                n=n-4;
                fil[j++]=5;
            }

            while(vCount[18]!=0)
            {
                vCount[4]--;vCount[18]--;vCount[4]--;vCount[21]--;vCount[13]--;
                n=n-5;
                fil[j++]=7;
            }

            while(vCount[8]!=0)
            {
                vCount[4]--;vCount[8]--;vCount[13]--;vCount[13]--;
                n=n-4;
                fil[j++]=9;
            }
        }
        sort (fil,fil+j);
        outFile<<"Case #"<<k+1<<": ";
        for (i=0;i<j;i++)
        {
            outFile<<fil[i];
        }
        outFile<<"\n";
    }
}
