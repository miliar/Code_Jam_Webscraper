#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
     ofstream outputFile;
    ifstream inputFile;
    inputFile.open("D-small-attempt1.in");
   outputFile.open("output.txt");
    int t,a=1;
    inputFile>>t;
    while(t>0)
    {
        long long k,c,s,i=1,x=1;
        inputFile>>k>>c>>s;
        for(int i=1;i<=c;i++)
            x*=k;
        outputFile<<"Case #"<<a<<": ";
        if(s!=k)
            outputFile<<"IMPOSSIBLE ";
        else if(c==1)
        {
            for(int i=1;i<=k;i++)
                outputFile<<i<<" ";
        }
        else{
        while(s>0&&(k*i)<=x)
        {
            outputFile<<(k*i)<<" ";
            s--;
            i++;
        }
        if(s>0)
            outputFile<<"1";
        }
        t--;
        a++;
        outputFile<<endl;
    }
    outputFile.close();
    return 0;
}
