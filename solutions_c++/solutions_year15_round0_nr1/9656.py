#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    ofstream myfile ;

     myfile.open("GCJ-1.txt") ;
 int t;
 cin>>t;
 int k=1;
 while(t--)
 {
     long int len;



     cin>>len;

     string s;
     cin>>s;
     long int people=0,ans=0;
     for(long int shyness=0;shyness<=len;shyness++)
     {
         if((s[shyness]-'0')>0)
         {

         if(people>=shyness)
         {
             people+=(s[shyness]-'0');
         }
         else
         {
          //  if(i==len)
            //{
                ans+=(shyness-people);
                people+=ans+s[shyness]-'0';
         }
         }

     }

     myfile << "Case #" << k << ": " << ans << endl;
     k++;
 }
}
