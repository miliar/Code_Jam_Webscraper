#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,l,i,p;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    for(p=1;p<=100;p++)
    {
        string s;
        long long int c=0,x=0;
        IF>>n>>s;
        l=s.length();
        for(i=0;i<l;i++)
        {
            if(s[i]!='0'&&i>c)
            {
                x+=i-c;
                c=i;
            }
            c+=int(s[i])-'0';
        }
        //cout<<"Case #"<<p<<": "<<x<<endl;
        OF<<"Case #"<<p<<": "<<x<<endl;
    }
    IF.close();
    OF.close();
    return 0;
}
