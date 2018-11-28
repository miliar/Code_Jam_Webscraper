#include <bits/stdc++.h>
#include <string>
using namespace std;
typedef  long int ll;

#define MAXLEN 1001



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);
    
	for(int i=0 ; i<t ; i++){
	
		string s,str;
		cin>>s;
		ll count=0,length=s.size();
		//bool fl=0;
		size_t found = s.find("-");
  		while (found!=string::npos)
  		{ //check for starting +ve before reversing
  		  ll k=0;
  		  bool fl=0;
  		  while(k<length){
  		  	if(s[0]=='-') break;
  		  	if(s[k]!='+' )
  		  	{   fl=1;
  		  		//reverse and move++
				for(ll z=0 ; z<k ;z++) s[z]='-';
				count++;
				
				break;
			}
			k++;

		  }
		  
		  if(k==length && fl==0){
		  	count++;
		  	for(ll z=0;z<length ; z++) s[z]='+';
		  }
		  else{
  		  
		  size_t lminus = s.find_last_of("-");
		  if (lminus!=string::npos){
		  	
		  	count++;

          str=s;
 
         

		   for(ll z=0 ; z<=lminus ;z++){
		  	s[z]=str[lminus-z];
		  	if(s[z]=='-') s[z]='+';
		  	else s[z]='-';
		  }	
		   
		   }
		  		
		  	  
		  } //else

		found = s.find("-");
		}
		printf("Case #%d: ",i+1);
		printf("%lld\n",count);
	}
		// printf("\n");	
    return 0;
}
