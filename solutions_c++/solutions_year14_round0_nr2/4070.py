#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;

int main()
{
	int t,count=1;
	long double tim1,tim21,tim22,tim2,c,f,x,rate,timprev;
	
	cin>>t;
	fstream fout;
	fout.open("op2.txt",ios::out);
	
	while(count<=t)
	{
		tim1=tim2=0;
		cin>>c>>f>>x;
		tim1=c/2;
		tim2=x/2;
		rate=2;
		fout.precision(7);
		fout.setf( std::ios::fixed, std:: ios::floatfield );
		if(tim2<tim1)
		    fout<<"Case #"<<count<<": "<<tim2<<endl;
		else{
			tim21=1;
			tim22=0;
			rate = 2 +f;
		while(tim21>tim22)
		{
			tim21=tim1+(x/rate);
			tim1+=c/rate;
			rate+=f;
			tim22=tim1 + (x/rate);
		}
			fout.precision(7);
			fout.setf( std::ios::fixed, std:: ios::floatfield );
			if(tim2<tim21)
			    fout<<"Case #"<<count<<": "<<tim2<<endl;
			else
		    fout<<"Case #"<<count<<": "<<tim21<<endl;
		
	}
	count++;
	}
	
	fout.close();
	return 0;
}
