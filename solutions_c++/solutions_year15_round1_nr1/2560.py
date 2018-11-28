#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t,n,i,j,y,z,max;
    ifstream infile ("A-large.in");
    ofstream outfile ("output.in");
    infile>>t;
    for(i=1;i<=t;i++)
    {
        y=0;
        max=0;
        z=0;
        infile>>n;
        int ara[n];
        for(j=0;j<n;j++)
        {
            infile>>ara[j];
            if(j>0 && ara[j]-ara[j-1]<0)
                {
                    y+=(ara[j-1]-ara[j]);
                    if(ara[j-1]-ara[j]>max)
                        max=ara[j-1]-ara[j];
                }


        }
          for(j=0;j<n-1;j++)
                {
                    if(ara[j]>=max)
                        z+=max;
                    else
                        z+=ara[j];
                }
        outfile<<"Case #"<<i<<": "<<y<<" "<<z<<endl;

    }
    return 0;
}
