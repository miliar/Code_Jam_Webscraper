#include <iostream>
#include <bits/stdc++.h>
using namespace std;


#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);

int main()
{
    READ("input.txt");
    WRITE("output.txt");
    int t;
    int counter=1;
    cin>>t;
    while(t--)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<counter<<": ";
        if(s>=k){
        for(int i=1;i<=s;i++)
        {
            cout<<i<<" ";

        }
        }
        else
            cout<<"IMPOSSIBLE";

        cout<<endl;
        counter++;
    }

    return 0;
}
