#include <bits/stdc++.h>
using namespace std;

string str;
set <string> ss;
void permute(string sxy, int l, int r)
{
   int i;
   if (l == r+1)
     {
          ss.insert(sxy);

     }
   else
   {
       char c=str[l];
       string r1=sxy;
       string r2="";
       r1+=c;
       r2+=c;
       r2+=sxy;
      permute(r1,l+1,r);
      permute(r2,l+1,r);
   }
}
int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int t;
   cin>>t;
   for(int tt=1;tt<=t;tt++)
        {
            ss.clear();
		 cin>>str;
		 int n=str.length();
		 string sassy="";
		 sassy+=str[0];
         permute(sassy, 1, n-1);
         set <string> :: reverse_iterator it;
         it=ss.rbegin();
         cout<<"Case #"<<tt<<": ";
         cout<<*it<<endl;
        }

        return 0;
}
