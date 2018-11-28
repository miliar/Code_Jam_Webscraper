#include <iostream>
#include<bits/stdc++.h>
using namespace std;
string s;
string solve(string q ,int pos)
{

   if(q.size() == s.size()) return q;


   return max(solve(q+s[pos] , pos+1) , solve(s[pos]+q , pos+1));
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    int j = 1;
    while(t--)
    {

        cin>>s;
        string q = "";
        q+=s[0];
        for(int i = 1 ; i<s.size() ; i++)
        {
            if(s[i]>=q[0]) q = s[i]+q;
            else q+=s[i];
        }
    printf("Case #%d: ",j++);
    cout<<q<<endl;
    }
    return 0;
}
