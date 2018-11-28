#include <iostream>
#include<string>
#include<stdio.h>
//#include<fstream.h>
using namespace std;

int main()
{
    freopen("A.in","r", stdin);
freopen("output.in","w", stdout);
   int   test,tt=1,n;
   cin>>test;

   while(test--)
   {
       string a,b;
        cin>>n;
        cin>>a;
        cin>>b;
        cout<<"Case #"<<tt<<": ";

        int i=0,j=0,f=0,cnt=0;
        while(i<a.size()&&j<b.size())
        {
            if(a[i]==b[j])
            {
                i++;j++; continue;
            }
            else
            {
                if(a[i]==a[i-1]) {cnt++;i++;}
                else if(b[j]==b[j-1]) {cnt++;j++;}
                else {f=1;break;}
            }
        }
        while(i<a.size())
        {
            if(a[i]==a[i-1]) {cnt++;i++;}
             else {f=1;break;}
        }
        while(j<b.size())
        {
             if(b[j]==b[j-1]) {cnt++;j++;}
             else {f=1;break;}
        }
        if(f==1) cout<<"Fegla Won"<<endl;
        else cout<<cnt<<endl;

        tt++;
   }
    return 0;
}
