#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long long int t,i,j,count,nop,n;
    cin>>t;
    int k=t;
    j=1;
    while(t--)
    {
        count=0;
        nop=0;
        cin>>n;
        char s[n+1];
        cin>>s;
        int l=strlen(s);
        for(i=0;i<=n;i++)
        {
            if(s[i]-48!=0)
            {
                if(count>=i)
                {
                    count+=s[i]-48;
                }
                else
                {
                    if(count==0)
                    {
                        nop+=i;
                        count+=nop;
                    }
                    else
                    {
                        nop+=i-count;
                        count+=nop;
                        //cout<<i<<" "<<count;
                    }

                    count+=s[i]-48;
                }
            }
           // cout<<count<<"\n";
        }
        cout<<"Case #"<<j<<": "<<nop<<"\n";
        j++;
    }
    return 0;
}
