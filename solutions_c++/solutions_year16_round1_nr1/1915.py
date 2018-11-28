#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
   cin.tie(false);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        string s;
        cin>>s;
        char arr[3000];
        int l=s.length();
        arr[1050]=s[0];
        int j=1050;
        int m=1050;
        char ch=s[0];
        for(int i=1;i<l;i++)
        {
           if(s[i]>=ch)
           {
              j=j-1;
              arr[j]=s[i];
              ch=s[i];
           }
           else
            {
                m=m+1;
                arr[m]=s[i];
            }
        }
        cout<<"Case #"<<k<<":"<<" ";
       for(int i=j;i<=m;i++)
        {
            cout<<arr[i];
        }
        cout<<"\n";
        k++;
    }
    return 0;
}
