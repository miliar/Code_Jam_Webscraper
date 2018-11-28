#include <iostream>
#include <bits/stdc++.h>
using namespace std;
string a="",maxi;
void solve(string s,int i,int n)
{
    if(i==n)
    {


        if(a.compare(maxi)>0)
        {
            maxi=a;
        }
        return;
    }
    a=a+s[i];
    solve(s,i+1,n);
    a.erase(a.length()-1,1);
    a=s[i]+a;
    solve(s,i+1,n);
    a.erase(0,1);
}
int main()
{
    ifstream ob;
    ob.open("A-small-attempt0 (1).in");
    ofstream ot;
    ot.open("out.txt");
    int i,t=0;
    string s,temp;
    //cin>>t;
     getline(ob,temp);
    for(i=0;i<temp.length();i++)
    {
        t*=10;
        t+=(temp[i]-48);
    }
    //cout<<t;
    for(i=1;i<=t;i++)
    {
        //cin>>s;
        getline(ob,s);
      //  cout<<s;
        int n=s.length();
        a=a+s[0];
        solve(s,1,n);
        a="";
        ot<<"Case #"<<i<<": "<<maxi<<endl;
        maxi="";

    }
    ob.close();
    ot.close();
    return 0;
}
