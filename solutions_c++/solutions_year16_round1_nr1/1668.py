#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;int x=1;
    while(t--)
    {
        string s;
        cin>>s;
        string ar;
        ar=s[0];
        for(int i=1;s[i]!='\0';i++)
        {
            if(s[i]<ar[0])
                ar=ar+s[i];
            else
                ar=s[i]+ar;
        }
        ar=ar+'\0';
        cout<<"Case #"<<x<<": "<<ar<<"\n";
        x++;
    }
}
