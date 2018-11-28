#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	int cases  = 0;
	while(t--)
	{
	     int num; 
		 scanf("%d",&num);
		 cases++;
		 string s;
		 cin>>s;
		 long long int sum =  s[0] - 48;
		 if(num==0)
		 {
		 	cout<<"Case #"<<cases<<": "<<0<<endl;
		 }
		 else
		 {
			long long int maxans =   0;
			long long int pans  =  0;
			 for(int i=1;i<=num;i++)
			 {
			 	     if((i -  sum)>0)
			 	     {
			 	     	 pans  =  (i -  sum);
						   if(pans>maxans)
						   {
						   	    maxans =  pans;
						   }    
			 	     }
			 	     sum   = sum  +  s[i] - 48;
			 }
			cout<<"Case #"<<cases<<": "<<maxans<<endl; 
		}
			 	
	}
	return  0;
}
