#include<bits/stdc++.h>
#include<fstream>
using namespace std;
long int number(char s[])
{
    int t=0;
    char *p;
    p=s;
    while(*p!=NULL)
    {
        t*=10;
        t+=(int)*p-48;
        p++;
    }
    cout<<t<<endl;
    return t;
}
int main()
{
    long long p;
    long int t,i,n,x,sum,j;
    char s[1001];
    char ch[10],c;
    int count;
    ifstream op("a1.txt");
    ofstream fp("a2.txt");
    op>>ch;
    t=number(ch);
    for(j=0;j<t;j++)
    {
        sum=count=0;
        op>>ch;
        n=number(ch);
        op>>s;
        for(i=0; i<n;i++)
        {

            x=(int)s[i] - 48;
            sum+=x;
            if(sum<i+1)
            {
                count++;
                sum++;
            }
        }
        fp<<"Case #"<<j+1<<": "<<count<<endl;
        cout<<"Case #"<<j+1<<": "<<count<<endl;
    }
    op.close();
    fp.close();
}
