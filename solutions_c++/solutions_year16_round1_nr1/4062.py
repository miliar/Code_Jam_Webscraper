#include <iostream>
#include <bits/stdc++.h>
#include <deque>
using namespace std;

int main()
{
    freopen("me.in","r",stdin);
     freopen("out.txt","w",stdout);
    int t;
    cin>>t;
   int count=0;
    char arr[2000];
   std::deque<char> brr;
    int s,l,r,xx;
    while(t--)
    {
        count++;
        cin>>arr;
        brr.push_back(arr[0]);
        for(int i=1;i<strlen(arr);i++)
        {
            s=(int)arr[i];
            l=(int)brr[0];
            r=(int)brr[brr.size()-1];
          //  cout<<"s="<<s<<" l="<<l<<" r="<<r<<endl;
            if(l<=s)
                brr.push_front(arr[i]);
                else
                    brr.push_back(arr[i]);
        }
        cout <<"Case #"<<count<<": ";
        for (deque<char>::iterator it = brr.begin(); it != brr.end(); ++it)
                cout <<*it;
                cout<<endl;
                brr.clear();
    }
}
