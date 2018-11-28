#include<iostream>
#include<cmath>
#include<fstream>
#include<cstring>
using namespace std;

ifstream input;
ofstream output;

string  from_binarynosystem_to_binary_string(long long int n) 
{
    long long int  i=1,binary=0;
    char rem;
    string str="",rev="";
    while (n!=0)
    {
        rem=(n%2);
        n/=2;
	if(rem)
	str+='1';
	else
	str+='0';
    }
	i=str.length();
	while(i--)
 	rev+=str[i];
	return rev;

}



long long int binary_string_to_system(string n,long long int system) 
{

	long long int decimal=0, j,i=0, rem;
	
	  for(i=n.length()-1, j=0;i>=0;i--,j++)
	 {
			if(n[i]=='1')
			  	   decimal=decimal+pow(system,j);  				
	}
	return decimal;
	
}

int main()
{

	string filter;
	long long int t_c,n,j,i,l,min,max,k,flag,counter,system,final_prime,divisor[10],generic,index,index1,var;
	input.open("C-small-attempt1.in");
	output.open("output.out");
	input>>t_c;

	for(i=1;i<=t_c;i++)
	{
		counter=0,final_prime=0;
		input>>n;
		input>>j;
		output<<"Case #"<<t_c<<":\n";		
				
		max=0;

		min=1+pow(2,n-1);
		for(l=0;l<n;l++)
		{
			var=pow(2,l);
			
			max+=var;
		}

		for(l=min;l<=max && final_prime<j;l++)
		{
			index=0;
			if(l%2!=0){
			filter=from_binarynosystem_to_binary_string(l); // to binary not binary system
			for(system=2;system<=10;system++)
			{
		
						
						generic= binary_string_to_system(filter,system);
						flag=1;	
						for(k=2;k<=sqrt(generic);k++)
						{
							if(generic%k==0)
							{
					
										flag=0;
										divisor[index]=k;
										index++;
										break;
							}

						} 
						if(flag==1)
							break;
						
				}
				if(system==11)
				{
					final_prime++;
					output<<filter;
					for(index1=0;index1<index;index1++)
						output<<" "<<divisor[index1];
					output<<"\n";
				}
			}
		}
	
	}
	input.close();
	output.close();

return 0;
}
