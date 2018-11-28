#include <iostream>
#include<fstream>
//#include<ostream>
using namespace std;

//#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif

	int run = 0;
	cin>>run;
	bool itrFlg = false;
	int iter = 0;
	while(run--)
	{
		if(itrFlg)
			cout<<endl;
		itrFlg = true;

		unsigned long long a=0,b=0;
		unsigned long long num=0,rev=0,lastDigit=0,check=0;
		long double sqroot1=0,sqroot2=0,sqroot_param=0;
		unsigned int palCount=0;
	
		cin>>a>>b;
	
		for (unsigned long long i=a;i<=b;i++)
		{
			num=i;
			lastDigit=0;
			rev=0;
			while(num>0)
			{
				rev=rev*10;
				rev=rev+num%10;
				num /=10;
			}		
			if (i==rev) 
			{
				//cout<<"First time :: Reverse is :: "<<rev<<" and Input is :: "<<i<<endl;
				//cout<<"PALINDROME :: "<<rev<<endl;			
				sqroot_param = rev;			
				sqroot1 = sqrt (sqroot_param);
				//cout<<"Sqr root1 is :: "<<sqroot1<<endl;
				check = sqroot1;
				//cout<<"Check value is :: "<<check<<endl;
				sqroot2 = check;
				//cout<<"Sqr root2 is :: "<<sqroot2<<endl;
				if(sqroot1 == sqroot2)
				{
					num = check;
					rev = 0;
					while(num>0)
					{
						rev=rev*10;
						rev=rev+num%10;
						num /=10;
					}				
					if (check == rev) 
					{
						//cout<<"Second time :: Reverse is :: "<<rev<<" and Input is :: "<<check<<endl;
						palCount++;
					}
				}
			}
		}
		//cout<<"Fair and sqr count is ::"<<palCount<<endl;

		//Result Display
		cout<<"Case #"<<++iter<<": "<<palCount;
	}

	return 0;
}