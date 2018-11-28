#include<bits/stdc++.h>
using namespace std;

bool a[10];

int main()
{
	long long int t,n,i,rem,m,c,j,k,flag,l;
	freopen("A-large.in","r",stdin);
	freopen("outputLarge.txt","w",stdout);
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		c=0,j=1;
		flag=0;
		if(n!=0){
		for(k=n;;k=n*j){
		    m=k;
		       while(k>0){
			              rem=k%10;
			               k=k/10;
			              if(a[rem]==false){
			             	a[rem]=true;
				             c++;
				          if(c==10){
					          flag=1;
					           break;
				               }
		                 	}
	                   	}
		            j++;
		            if(flag==1){
		            	cout << "Case #" << i << ": " <<m<< endl;
		            	break;
					}
		
	        }   
	    }else
	         	cout << "Case #" << i << ": " <<"INSOMNIA"<< endl;
	         	for(l=0;l<10;l++)
	         	a[l]=false;
	}
	return 0;
}
