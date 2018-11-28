#include<iostream>

#include<cstdio>

using namespace std;

int main()
{
	FILE *in=freopen("A-large.in","r",stdin);

  	FILE *out =freopen("sheeplarge.txt","w",stdout);
  	
  	int test,ptest;
	  long int no;
	  cin>>test;
	  ptest=test;
	while(test>0)
	{
		int sum=0;
		long int fno,temp;
		int rem;
		int arr[10];
		for(int i=0;i<10;i++)
			arr[i]=0;
		cin>>no;
		temp=no;
		long int i=1;
		if(no==0)
			cout<<"Case #"<<(ptest-test)+1<<":"<<" "<<"INSOMNIA"<<endl;
			
		else
		{
			
			while(sum!=10)
			{
				
				temp=no * i;
				fno=temp;
				
				while(temp>0)
				{
				
					rem=temp%10;
					if(arr[rem]==0)
					{
						arr[rem]=1;
						sum+=1;
					}
					temp=temp/10;
				}
				
				i++;
			}
			cout<<"Case #"<<(ptest-test)+1<<":"<<" "<<fno<<endl;
		
		}
		test--;
	  }
	  fclose(in);
fclose(out);
	  
	  return 0;  
}
