#include <bits/stdc++.h>
using namespace std;

set <string >sec;
string radix_bin(ll inc)
{
   long long i ,j , k ;
  string answer="";
  while(inc)
  {
  	if(inc%2)
  		answer=answer+"1";
  	else
  		answer=answer+"0";
  	inc>>=1;
  }
  reverse(answer.begin(),answer.end());
  return answer;
}

int main()
{
   freopen("choot.txt","w",stdout);
   long long i ,n=3;
   long long ankur=1;

   long long raja=(2147483649);
   i=0;
   long long count=0,answer,ek=0;
   
   cout<<"Case #1:"<<endl;
   
   while(true)
 	{   
 	 if(count>=500)break;
 	 answer=raja+i*6;
 	 i+=1;
 	 string s=radix_bin(answer);
 	 for(int j=0;s[j]!='\0';j+=1)
 	 if(s[j]=='1')ek++;
 	 if(ek%2==0)
 	 {
 	  cout<<s<<" 3 2 5 2 7 2 3 2 11"<<endl;
          count++;
 		}
 	 ankur+=1;
 	 ek=0;
 	}



	return 0;
}
