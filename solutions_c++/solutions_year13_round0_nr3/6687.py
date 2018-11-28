#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
ifstream file("input.txt");
int testno=0;

long double start_num,end_num;
/*
3
1 4
10 120
100 1000
*/

int check_sqr(long double num)
{
	long double sqr = sqrt(num);
	if(start_num<= sqr <=end_num)
		return sqr;
	else 
		return -1;
}

int check_palin(long double num)
{
	int reverse=0, rem, temp;
	
	temp=num;
	while(temp!=0)
	{
		rem = temp % 10;
		reverse=reverse*10+rem;
		temp/=10;
	}  


	if(reverse==num)  
	{	
		return num;
	}	
	else
		return -1;

}

int main()
{
	file>>testno;
	

	for(int i=0;i<testno;i++)
	{
		file>>start_num>>end_num;
		/*cout<<"Start Range: "<<start_num<<" & ";
		cout<<"End Range: "<<end_num<<endl;*/
		long double count = 0;
		for (long double x = start_num; x <=end_num; x++)
		{
			long double flagA = check_palin(x);
			long double sqr = sqrt(x);
			long double flagB = check_palin(sqr);
			if (flagA>-1 && flagB>-1)
			{
				/*cout<<x<<endl;*/
				count++;
			}
		}
		if(i!=0)
			cout<<endl;
		cout<<"Case #"<<i+1<<": "<<count;
		
	}

	file.close();

	return 0;
}
