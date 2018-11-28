#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<cmath>
#include<fstream>
#include<stdio.h>
#include<ctype.h>
#include<sstream>
#define loop(i,n) for(int i=0;i<n;i++)
#define loopto(f,l) for(int j=f;j<=l;j++)

using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("output.txt");

    long long t,s,n;
    in>>t;
    string ss;
    for(int k=0;k<t;k++)
    {
        in>>s;
        long long a[s],sum=0,c=0;
        in>>ss;
        loop(i,ss.length())
        {
            if(sum<i)
            {
                sum++;sum+=ss[i]-48;
                c++;
            }
            else
            {
                sum+=ss[i]-48;
            }
        }//cout<<sum<<endl;
        out<<"Case #"<<k+1<<": "<<c<<endl;
    }

    return 0;
}
