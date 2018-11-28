#include <iostream>
#include <list>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>

using namespace std;

bool a[100];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >>t;
    for(int q=1;q<=t;q++)
    {
        cout <<"Case #"<<q<<": ";
        int n;
        cin >>n;
        long long m = n;
        for(int i=0;i<10;i++)
            a[i] = false;
        bool ok  =false;
        for(int i=0;i<1e5;i++)
        {
            long long t = m;
            while(t){a[t%10] = true; t/=10;}
            for(int i=0;i<10;i++)
            if(a[i])t++;
            if(t==10) {cout << m<<endl; ok = true; break;}
            m+=n;
        }
        if(!ok) {cout <<"INSOMNIA"<<endl;}
    }
    return 0;
}

