#include <iostream>
#include<string>
#include<cstdio>
using namespace std;
 string s;

int main()
{

        freopen("input_file_large.in","r",stdin);
    freopen("output_file_large.out","w",stdout);


 int len,i,t,j;
 cin>>t;

 for(i=1;i<=t;i++)
 {
     cin>>s;
     len= s.length();
  // cout<<"length:"<<len<<endl;

     for(j=1;j<len;j++)
     {

         if((int)(s[j])>=(int)(s[0]))
         {
            //           shif(j,s);

             char te = s[j];
                s.insert(s.begin()+0,te);
         //       cout<<" add "<<s<<endl;
                //len++;
                s.erase(s.begin()+(j+1));
                //len--;
           //cout<<"erase "<<s<<endl;
         }


     }

     cout<<"Case #"<<i<<":"<<" "<<s<<endl;
 } //test

    return 0;
}

