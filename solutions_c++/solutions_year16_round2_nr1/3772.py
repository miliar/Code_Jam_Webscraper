#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int k=0;
    while(t--)
    {
        k++;
        string arr[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
        string s;
        cin>>s;
        vector<int> v;
        for(int i=0;i<=10000000;i++)
        {
             v.clear();
            int n=i;
            string st="";
            int d;
           while(n!=0)
           {
               d=n%10;
               n=n/10;
               st=st+arr[d];
               v.push_back(d);
           }

        if(st.length()>s.length())
            continue;
    int  p=s.length()-st.length();

        if(p%4==0)
        {
            for(int k=0;k<(p/4);k++)
            {
                st=st+arr[0];
                v.push_back(0);
            }
        }
        else
            continue;
         sort(st.begin(),st.end());
        sort(s.begin(),s.end());
        if(s==st)
            break;
    }
    sort(v.begin(),v.end());
      cout<<"Case #"<<k<<": ";
    for(int i=0;i<v.size();i++)
      cout<<v[i];
        cout<<"\n";

    }
}
