#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,l,i,j,k=1,a,answer;
    string s;
    ifstream in;
    ofstream out;
    in.open("abc.txt");
    out.open("abc2.txt");
    in>>t;
    while(t--)
    {
        in>>s;
        l=s.length();
        i=0;
        answer=0;
                while(s[i]=='-'&&i<l)
                {
                    i++;
                    answer=1;
                }
                while(i<l)
                {
                    while(s[i]=='+'&&i<l)
                    {
                       i++;
                    }
                    if(s[i]=='-')
                    {
                        answer+=2;
                        while(s[i]=='-'&&i<l)
                        i++;
                    }
                }
        out<<"Case #"<<k<<": "<<answer<<endl;
        k++;
    }
    return 0;
}
