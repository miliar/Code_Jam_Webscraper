#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
        ofstream outputFile;
    ifstream inputFile;
    inputFile.open("A-large.in");
   outputFile.open("output.txt");
    int t,n=1;
    inputFile>>t;
    while(t>0)
    {
        string s;
        inputFile>>s;
        vector <char> v;
        char x=s[0];
        for(int i=0;i<s.length();i++)
        {
            if(s[i]>=x)
            {
                x=s[i];
                v.insert(v.begin(),x);
            }
            else
                v.push_back(s[i]);
        }
        outputFile<<"Case #"<<n<<": ";
        for(int i=0;i<s.length();i++)
            outputFile<<v[i];
        outputFile<<endl;
        n++;
        t--;
    }
    outputFile.close();
    return 0;
}
