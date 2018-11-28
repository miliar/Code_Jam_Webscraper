#include<iostream>
#include<string>
#include<fstream>
#include<math.h>

using namespace std;

bool balind(int num)
{
	int a,sum=0;
	int num1=num;
  
   
    
	  while(num!=0)    
      {
        a=num%10;
        num=num/10;
        sum=sum*10+a;
     }
    if(sum==num1)
    return 1;
    else return 0;
  
}	

int main()
{
	ifstream in("raw.in");
	ofstream out("raww.txt");
	long long t;
	in>>t;
	for(long long i = 0 ; i < t; i++)
	{
		long long a,b;
		long long count;
		count =0;
		in>>a>>b;
		long double result;
		long long  res;
		for(long long j=a ; j<=b; j++){
			result = sqrt (j);
			res = (int )result;
			if(result - res == 0){
				int z = balind(j);
				if(z == 1){
					if(balind(result) == 1)
						count++;
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<count<<endl;
		
	}
	return 0;
}
