#include <iostream>
#include <cstring>
using namespace std;
string st;
int a[2000];
int b[2000];
int K;

int main()
{
int T;
int t;

cin>>T;
t=T;
while(T--)
{
   int sum=0;
   cin>>st;
   cin>>K;
   for(int i=0;i<st.length();i++)
   {a[i]=(st[i]=='+')?0:1;}
    
	for(int i=0;i<=st.length()-K;i++)
    {
	 if(a[i]==1) {for(int j=0;j<K;j++) a[i+j]=(a[i+j]+1)%2; sum++;}
	 
    }
 
   
   
   bool ok=true;
   for(int i=st.length()-K+1;i<st.length();i++)
   {
   	  if(a[i]%2!=0) {ok=false; break;}
    
   }
   cout <<"Case #"<<t-T<<": ";
   if(ok==false) cout <<"IMPOSSIBLE";
   else cout << sum;
   if(T>=1) cout<<endl;	
	
	
}


return 0;

}
