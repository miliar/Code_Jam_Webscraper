#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
    ifstream in("A-large.in");
    ofstream out("sheeps_large.txt");
    int t;
    in>>t;
    for(int i=1; i<=t; ++i)
    {
        char ch[100];
        ll A[]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        ll n, st=1, c=10, temp, l, k;
        in>>n;
        while(c)
        {
            temp=st*n;
            itoa(temp, ch, 10);
            l=strlen(ch);
            for(int j=0; j<l; ++j)
            {
                k= ch[j]-'0';
                if(A[k]==0)
                {
                    A[k]=1;
                    c--;
                }
            }
            st++;
            if(st>100)
            {
                out<<"Case #"<<i<<": INSOMNIA"<<endl;
                break;
            }
        }
        if(st<=100)
            out<<"Case #"<<i<<": "<<temp<<endl;
    }
    return 0;
}
