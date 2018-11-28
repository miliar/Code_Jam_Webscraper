#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in("A-large.in");
    streambuf *cinbuff = cin.rdbuf();
    cin.rdbuf(in.rdbuf());

    ofstream out("out");
    streambuf *coutbuf = cout.rdbuf();
    cout.rdbuf(out.rdbuf());

    int t,T,s,l,i;
    int c,n,a,sum;
    char st[1001];
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>s>>st;
        l=strlen(st);
        c=0;
        n=0;
        a=0;
        sum=0;
        for(i=0;i<l;i++)
        {
            if(a<c)
            {
                sum+=(c-a);
                a+=(c-a);
            }
            n=st[i]-48;
            a+=n;
            c++;
        }
        cout<<"Case #"<<t<<": "<<sum<<endl;
    }
}
