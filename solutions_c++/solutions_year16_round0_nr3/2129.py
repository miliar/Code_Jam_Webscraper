#include <bits/stdc++.h>
using namespace std;
#define ll long long 
#define fi first 
#define se second
#define pb push_back  
#define mp make_pair
set <string >sec;
string to_bin(ll inc)
{
   ll i ,j , k ;
  string ans="";
  while(inc)
  {
  	if(inc%2)
  		ans=ans+"1";
  	else
  		ans=ans+"0";
  	inc>>=1;
  }
  reverse(ans.begin(),ans.end());
  return ans;
}

int main()
{
	freopen("hihi.txt","w",stdout);
   ll i ,n=3;
   ll cn=1;

   ll con=(2147483649);
   i=0;
   ll cnt=0,ans,one=0;
   cout<<"Case #1:"<<endl;
 	while(1)
 	{   //if(cn==315){cn++;i++;continue;}
 		if(cnt>=500)break;
 		ans=con+i*6;
 		i+=1;
 		string s=to_bin(ans);
 		for(int j=0;s[j]!='\0';j+=1)
 			if(s[j]=='1')one++;
 		if(one%2==0)
 		{cout<<s<<" 3 2 5 2 7 2 3 2 11"<<endl;cnt++;}
 	cn+=1;
 	one=0;
 	}

//cout<<sec.size();


	return 0;
}