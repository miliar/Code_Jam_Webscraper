#include<iostream>
#include<math.h>
using namespace std;
int main()
{
int number;
int opt[2],flag[11],div[500][11];
int j,count_of_numbers=0;

cin>>number;			//Input of number of trials
cin>>opt[0];
cin>>opt[1];		//Accepting Parameters
int p,ep,pr_no[32],q;

cout<<"Case #1:\n";  		//Display Case Number

//Setting Initial value of Number to 10000000....
for(p=0;p<opt[0];p++)
	pr_no[p] = 0;
pr_no[opt[0]-1] = 1;


//The eternal script
while(true)
{
	int base,pr;

	//Sets flag to 0
	for(ep=0;ep<11;ep++)
		flag[ep] = 0;

	//Generation of number
	for(ep=0;ep<opt[0]-1;ep++)
	{
		if(pr_no[ep] == 0)
			{pr_no[ep] = 1;break;}
		else
			{pr_no[ep] = 0;}
	}
	if(pr_no[0] == 0)
	{
		pr_no[0] = 1;
	}
	
	//Testing for all bases(2-10)
	for(base = 2;base <= 10;base++)
	{
		//Converting number to decimal
		unsigned long long int dec_number=0;
		for(q=0;q<opt[0];q++)
		{
			dec_number = dec_number + (pr_no[q] * pow(base,q));
			
		}
		//check if prime, set number as flag
		for(pr = 2;pr<dec_number;pr++)
		{
			if(dec_number%pr == 0)
				{flag[base] = dec_number;div[count_of_numbers][base] = pr;break;}
		}
	}



		//If all flags set, display number, display factor. Increment count by 1
		for(pr = 2;pr <=10 ; pr++)
		{
			if(flag[pr] == 0)
				{break;}
		}
		if(pr == 11)
		{
			for(p=opt[0]-1;p>=0;p--){cout<<pr_no[p];}
			for(base = 2;base < 11;base++)
			{
				cout<<" "<<div[count_of_numbers][base];
			}
			cout<<endl;
			count_of_numbers++;
		}


		//If count > opt[1], break.
		if(count_of_numbers >= opt[1])
			{break;}
	}

return 0;
}
