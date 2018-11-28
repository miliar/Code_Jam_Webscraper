#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<cstring>
using namespace std;
int main(void)
{
    freopen("output.txt","w",stdout);
    freopen("B-small-attempt0.in","r",stdin);
    int c=1, t;
    cin>>t;
    while(c<=t)
    {
        int a, b, k;
        int i, j, cnt=0, q;
        cin>>a>>b>>k;
        for (i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                q=i&j;
                //cout<<q<<" "<<k<<endl;
                if(q<k)    cnt++;
            }
        }
        cout<<"Case #"<<c<<": "<<cnt<<endl;
        c++;
    }
    fclose(stdout);
    fclose(stdin);
}
