#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    FILE *in=fopen("A-small-attempt0.in","r");
    FILE *out=fopen("output.txt","w");
    int n,sm,r,st,sum=0,l;
    vector <int> s,ans;
    fscanf(in," %d",&n);
    for(int i=0;i<n;i++)
    {
        s.clear();
        s.resize(1000,0);
        s.clear();
        l=0;
        sum=0;
        fscanf(in," %d",&sm);
        fscanf(in," %d",&st);
        while(st>0)
        {
            r=st%10;
            st=st/10;
            s.push_back(r);
        }
        for(int k=sm-1;k>=0;k--)
        {
            sum+=s[k+1];
            while((sm-k)-sum>0)
            {
                sum++;
                l++;
            }
        }
        ans.push_back(l);
    }
    for(int i=0;i<n;i++)
        fprintf(out,"Case #%d: %d\n",i+1,ans[i]);
        fclose(in);
        fclose(out);
    return 0;
}
