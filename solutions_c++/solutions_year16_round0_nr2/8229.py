#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream outputFile;
    ifstream inputFile;
    inputFile.open("B-small-attempt3.in");
   outputFile.open("output.txt");
    int t,n=1;
    inputFile>>t;
    while(t>0)
    {
        string c;
        int counter=0;
        int x=0;
        inputFile>>c;
       for(int i=c.length()-1;i>=0;i--)
       {
           if(c[i]=='-')
           {
               counter++;
               x=i;
               for(int j=0;j<=x;j++)
               {
                   if(c[j]=='-')
                    c[j]='+';
                   else
                    c[j]='-';
               }
           }
       }
        outputFile<<"Case #"<<n<<": "<<counter<<endl;
    n++;
        t--;
    }
    outputFile.close();
        return 0;
}
