#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
 ofstream output ;

 output.open("1.txt") ;

 long long int T,j=1;
 cin>>T;

 while(T--)
 {
     long long int length,p=0,ans=0;
     string s;
     cin >> length >> s;
     for(long long int i=0;i<=length;i++)
     {
         if((s[i]-'0')>0)
         {

         if(p>=i) p+=(s[i]-'0');
         else
         {
                ans+=(i-p);
                p+=(i-p)+s[i]-'0';
         }

         }
     }

     output << "Case #" << j << ": " << ans << endl;
     j++;
 }
 return 0;
}

