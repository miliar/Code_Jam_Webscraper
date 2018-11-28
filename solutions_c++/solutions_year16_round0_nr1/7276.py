#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int T;
	long N;
        int index = 1;		
	ifstream infile;
	infile.open("A-large.in", ios::in);
	
	ofstream outfile;
	outfile.open("largeOutput0.out", ios::out);
 
	long long temp; // for holding the value of number named
	int digit;// to store digits from a no.
	
	infile>>T;

	while(index<=T)
	{
	infile>>N;
	int i;
	
	if(N!=0)
	{
	int digiArr[10]={0};
	int count = 0;// Count of nos. seen till now

	for(i=1; count<10; i++)
	{
		temp = i*N;
		
		while(temp>0)
		{
			digit = temp%10;
			
			if(digiArr[digit] == 0)
			{
				digiArr[digit]++;
				count++;
			}
			
			temp=temp/10;			

		}

	}

	outfile<<"Case #"<<index<<": "<<N*(i-1)<<"\n";
	}
	else
		outfile<<"Case #"<<index<<": "<<"INSOMNIA\n";

	index++;
	}
	
	outfile.close();
	infile.close();
	return 0;
}
