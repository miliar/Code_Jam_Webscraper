#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream file;
    file.open ("a");
    int t;
    cin>>t;
    set<int>s;
    int con;
    for(int i=0; i<t; i++)
    {
        int n,j=1;
        cin>>n;
        con=n;
        if(n==0)
        {
            file<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        while(s.size()<10)
        {
            while(n>0)
            {
                int d=n%10;
                s.insert(d);
                n/=10;
            }
            j++;
            n=con*j;
        }
        if(s.size()==10)
            file<<"Case #"<<i+1<<": "<<n-con<<endl;
        s.clear();
    }
file.close ();
        return 0;
}
