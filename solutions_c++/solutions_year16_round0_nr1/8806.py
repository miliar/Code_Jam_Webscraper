#include<iostream>
using namespace std;

 main()
 {
 	long long t,temp,n;
 	cin>>t;
 	long long a[10];
 	long long x=1;
 	for(long long i=0;i<t;i++)
 	{
 		for(long long j=0;j<10;j++)
 			a[j]=-1;
 		cin>>n;
 		long N=n;
 		if(n==0){
 			cout<<"Case #"<<i+1<<": INSOMNIA\n";
 		}
 		
 		else
 		{
 			long long end=0;
 			x=1;
 			while(end==0){
 						
			 			n=N;
			 			n*=x;
			 			x++;
			 			while(n!=0)
						{
							temp=n%10;
							n=n/10;
							for(long long j=0;j<10;j++)
								if(temp==j)
									a[j]=1;
						}
						if(a[0]==1 && a[1]==1 && a[2]==1 && a[3]==1 && a[4]==1 &&
								a[5]==1 && a[6]==1 && a[7]==1 && a[8]==1 && a[9]==1){	
							 	cout<<"Case #"<<i+1<<": "<<N*(x-1)<<endl;
							 	end=1;
					
							}

			 		}

			 	}
			 }
}
