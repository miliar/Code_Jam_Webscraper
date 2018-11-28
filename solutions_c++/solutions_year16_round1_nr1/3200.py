#include<bits/stdc++.h>
using namespace std;
string s,temp,temp2;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("E:/A-large.in", "r", stdin);
	freopen("E:/output.txt", "w", stdout);
    int t,l,r,i,j,n,pos;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        n=s.length();
        l=r=s[0]-'A';
        temp.clear();
        temp2.clear();
        temp+=s[0];
        for(j=1;j<n;j++)
        {
           pos=s[j]-'A';
           //cout<<l<<" "<<r<<" "<<pos<<"\n";
           if(pos>=r)
           {
             temp2.clear();
             temp2+=s[j];
             temp2+=temp;
             temp.clear();
             temp+=temp2;
           }
           else
           {
               //cout<<"Going here ADDING "<<s[i]<<"\n";
               temp+=s[j];
           }
           l=min(l,pos);
           r=max(r,pos);
           //cout<<temp<<"\n";
        }
        cout<<"Case #"<<i<<": "<<temp<<"\n";
    }
    return 0;
}
