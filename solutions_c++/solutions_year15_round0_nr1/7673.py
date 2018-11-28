#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    char uu;
	long long int er,ans,tc,knock,ert,hogaya,anedo,pogo;
	
	
	scanf("%lld",&tc);
	uu=getchar();
	knock=0;
	while(knock!=tc)
	{	knock++;
	    ans=0;
		scanf("%lld",&er);
		uu=getchar();
		
		pogo=0;
		
		ert=0;
		while((uu=getchar())!='\n')
		{	
		    if(uu==48){
		        anedo=0;
		    }
		    else{
		        anedo=pogo;
		    }
			
			hogaya=anedo-ans;
		
			if(hogaya<=0){
	//done
			ans+=uu-48;
			}
			else
			{	ans+=hogaya+(uu-48);
			    ert+=hogaya;
			}
			//rehna hai tere dil me
			pogo++;
		}
		cout<<"Case #"<<knock<<": "<<ert<<endl;
		
	}
	return 0;
}
