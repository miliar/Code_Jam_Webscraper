#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include <fstream>
#include<vector>

using namespace std;

int main()
{
ifstream in; //Creating object for input stream
ofstream out; //Creating object for output stream

in.open("input.in");    //open a file to read input
out.open("outs.txt"); //open a file to write output

    long long t,n,p,xx,i,x,y,pi[27];
    string s;
    vector<string> rans;
    in>>t;
    for(xx=1;xx<=t;xx++)
    {
        rans.clear();
        in>>n;
        memset(pi,0,sizeof pi);
        for(i=1;i<=n;i++)
            in>>pi[i];
        while(1)
        {
            for(x=1;x<=n&&pi[x]==0;x++);
            if(x<=n)
            {
                for(y=x+1;y<=n&&pi[y]==0;y++);
                if(y<=n)
                {
                    s.clear();
                    s.push_back('A'+x-1);
                    s.push_back('A'+y-1);
                    rans.push_back(s);
                    pi[x]--;
                    pi[y]--;
                }
                else
                {
                    s.clear();
                    s.push_back('A'+x-1);
                    rans.push_back(s);
                    pi[x]--;
                }

            }
            else
                break;
        }
        out<<"Case #"<<xx<<": ";
        for(x=rans.size()-1;x>=0;x--)
            out<<rans[x]<<" ";
        out<<endl;
	}

in.close();             //closing the input file
out.close();            //closing the output file

    return 0;
}
