
#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;
char s[1000];


int main()
{


    freopen("input.in","r",stdin);
    freopen("output_file_large.out","w",stdout);

    int i,t,l,cnt=0;
    cin>>t;

    for(i=1;i<=t;i++)
    {

        cnt=0;
      cin>>s;
      l=strlen(s);

     cout<<"Case #"<<i<<": ";

     int j,k;

     for(j=0;j<l-1;j++)
     {
         if(((s[j]=='+'&&s[j+1]=='+')||(s[j]=='-'&&s[j+1]=='-')))
         {
             cnt = cnt+0;
         }
         else{
            cnt++;
         }

     }

            cnt++;
       if(s[l-1]=='+')
        cnt--;

        cout<<cnt<<endl;
        cnt=0;
    }


    return 0;
}
