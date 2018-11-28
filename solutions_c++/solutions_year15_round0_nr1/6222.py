/*shubham54*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <climits>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <cmath>
#include <fstream>
using namespace std;

int main()
{
    ofstream myfile;
    myfile.open("shub1.txt");
    long long int i,tot,sum,t,S,k=0;
    string s;
    cin>>t;
    while(t--)
    {
        ++k;
        cin>>S>>s;
        sum=0;tot=0;
        long long int a[2000]={0};
    for(i=0;i<s.length();i++)
        {
            a[i]=s[i]-48;
        }
    for(i=0;i<=S;i++)
    {
        if(i==0&&a[i]==0)
        {
           sum=1; tot=1;
        }
        else
        {
            if(a[i]!=0)
            {
                if(tot>=i||tot==0)
                    tot=tot+a[i];
                else
                {
                    sum=sum+(i-tot);
                    tot=tot+(i-tot);
                    tot=tot+a[i];

                }
            }

        }

        }
        myfile<<"Case #" << k <<": "<<sum <<endl;
    }
    return 0;
}
