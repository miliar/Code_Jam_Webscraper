#include <iostream>
#include <string.h>
#include <cstring>
#include <cmath>

using namespace std;

string revvv(string a,long long int i,long long int k)
{
    for(int p=i,y=k;y>=p;p++,y--)
    {
        if(p!=y)
        {
            if(a[p]=='+')
                a[p]='-';
            else
                a[p]='+';
        }
         if(a[y]=='+')
                a[y]='-';
            else
                a[y]='+';
        swap(a[p],a[y]);
    }
    return a;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outerr.in","w",stdout);
    long long int t;
    cin>>t;
    long long int cases = t;
    while(t--)
    {
        string a;
        cin>>a;
        long long int len=a.size()-1;
        long long int counter=0;
        while(len>=0)
        {
            long long int k=len;
            while(a[k]=='+')
            {
                k--;
            }
            len=k;
            if(len>=0)
            {
                int i=0;
                while(a[i]=='+')
                {
                    i++;
                }
                if(i)
                {
                    a=revvv(a,0,i-1);
                    counter++;
                }
                a=revvv(a,0,len);
                counter++;
            }
        }
    cout<<"Case #"<<cases-t<<": "<<counter<<endl;
    }
return 0;
}
