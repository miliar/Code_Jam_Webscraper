#include <bits/stdc++.h>
using namespace std;
int main()
{

 int t,n,i,c,f,r=1;
 string s;
 cin>>t;
 while(t--){
	 cin>>n>>s;
	 for(i=0,c=0,f=0;i<s.size();i++)
	 {
		 if(c-i>=0)
			 c+=(s[i]-48);
		 else{
			 if((s[i]-48)>0)
			 {f+=abs(c-i);
			 c+=f;
			 c+=(s[i]-48);
			 }
		 }
	 }
	 cout<<"Case #"<<r++<<": "<<f<<endl;
 }
 return 0;
}
