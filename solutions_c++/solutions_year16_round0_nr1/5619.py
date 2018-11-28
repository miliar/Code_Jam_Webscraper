#include<iostream>
#include<string.h>
using namespace std;
#define max 500
int get_no(long long int a)
{
	if(a==0){
		return 0;
	}

	else
	{


	    int s[10];
	    for(int m=0;m<10;m++)
	    {
		   s[m]=-1;
	    }
    	for(int i=1;i<max;i++)
		{
		   int temp=i*a;
	    	int S=temp;

			while(S!=0)
			{
				int res=S%10;
				s[res]=res;

			    S=S/10;
		    }
		  int flag=0;
		for(int k=0;k<10;k++)
		{
			if(s[k]!=-1)
			{
				flag=1;
			}
			else
			{
			    flag=0;
			    break;
			}

	   }
	   if(flag==1)
	   {
			//	cout<<temp<<endl;
				return (temp);
		}
	    }
}


//	return 0;
}

int main(){
	long long int T,N;
	cin>>T;
   for(long long int i=1;i<=T;i++)
   {
   	  cin>>N;
      int num= get_no(N);
	  if(num!=0)
	  cout<<"case #"<<i<<":"<<" "<<num<<endl;
	  else
	  cout<<"case #"<<i<<":"<<" "<<"INSOMNIA"<<endl;
   }
	return 0;
}
