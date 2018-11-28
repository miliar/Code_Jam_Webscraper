#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <sstream>
using namespace std;
int check_pal(string d)
{  int n=d.length(),i;
    //if(d.length()%2==0)
      
	for(i=0;i<n/2;i++)
	if(d[i]!=d[(n-1)-i])
	return 0;
return 1;
}

int main()
{ 
	long long int t,count,n,l,tmp,a,b,i;
     stringstream ss;string s;
     //char a[1000],b[1000];
	cin>>t;
	for(l=1;l<=t;l++)
	{   count=0;
		cin>>a>>b;
		tmp=sqrt(a);
		if((tmp*tmp)<a)
		tmp++;
		b=sqrt(b);
		for(i=tmp;i<=b;i++)
		{   ss.str("");
			ss<<i;
			s=ss.str();
			if(check_pal(s))
			{ss.str("");
			ss<<(i*i);
			s=ss.str();
			if(check_pal(s))
			{count++;//cout<<i<<" "<<i*i<<endl;
			}
			
		
		}
		
	}	
	printf("Case #%lld: %lld\n",l,count);
	
}
return 0;
}
