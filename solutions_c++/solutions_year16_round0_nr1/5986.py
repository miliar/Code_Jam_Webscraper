#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	long long int n,i,num,inr,mul_num,actual_num,t_c,counter_ten;
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.out");
	input >> t_c;
	for(i=1;i<=t_c;i++)
	{
		int count[10]={0};
		inr=1;
		input >> num;
		if(num==0)
			output<< "Case #"<<i<<": INSOMNIA\n";
		else
		{
			counter_ten=0;
			actual_num=num;
			while(counter_ten!=10)
			{
				
				num=actual_num*inr;
				mul_num=num;
				while(num>0)
				{
					count[num%10]=1;
					num/=10;
			
				}
				for(counter_ten=0;counter_ten<10;counter_ten++)
				{
					if(count[counter_ten]==0)
						break;		
				}
				inr++;
			}
			if(counter_ten==10)
			{
				output<<"Case #"<< i<<": "<<mul_num<<"\n";
			}
			
		}
	}
	input.close();
	output.close();
	return 0;
}