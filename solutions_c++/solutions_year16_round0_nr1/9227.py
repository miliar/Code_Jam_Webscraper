#include<stdio.h>
#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{  int num=0,last=0,nextnum=0,check=0,count=0,n0=0,n1=0,n2=0,n3=0,n4=0,n5=0,n6=0,n7=0,n8=0,n9=0;
	   //scanf("%d",&num);
	   cin>>num;
	   //cout<<"number="<<num<<"\n";
	   if(num==0)
		{ cout<<"Case #"<<i<<": "<<"INSOMNIA\n";}
	   else
		{
		do{ //cout<<"looping again";
			count=count+1;
			nextnum=count*num;
			last=nextnum;
			do{
				if(nextnum<10)
				{
					check=nextnum;
					nextnum=-1;
				}
		  else
				{
					check=nextnum%10;
				
					nextnum=nextnum/10;
						//cout<<"check="<<check<<"nextnum is="<<nextnum<<"\n";
				}
		  switch(check)
					{
						case 0:n0=1;
								break;
						case 1:n1=1;//cout<<"one selected";
								break;
						case 2:n2=1;
								break;
						case 3:n3=1;//cout<<"three selected";
								break;
						case 4:n4=1;
								break;
						case 5:n5=1;
								break;
						case 6:n6=1;
								break;
						case 7:n7=1;
								break;
						case 8:n8=1;
								break;
						case 9:n9=1;
								break;
					}
			
			}while(nextnum>0);
				
		  }while(n0==0 || n1==0 || n2==0 || n3==0 || n4==0 || n5==0 || n6==0 || n7==0 || n8==0 || n9==0 );
			cout<<"Case #"<<i<<": "<<last<<"\n";
		}

	}


    return 0;
}
