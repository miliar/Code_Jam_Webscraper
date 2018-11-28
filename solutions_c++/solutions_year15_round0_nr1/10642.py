#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

#define InputOutputToFile


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

	int count =0;

	vector<int> vl;
	
	bool itrFlg = false;
	int tc=1;
	int Smax=0,i=0;
	char C0='0';
	int soc=0,si=0;
	while(run--)
	{
		if(itrFlg)
		{
			count=0,i=0;
			soc=0,si=0;
			vl.clear();
			cout<<endl;
		}
		itrFlg = true;
		cin>>Smax;
		char c;
		for(i=0;i<=Smax;i++)
		{
			cin>>c;
			vl.push_back(c-C0);
		}

		for(i=0;i<=Smax;i++)
		{
			si=i;
			if(vl[si]>0 && soc<si)
			{
				count+=si-soc;
				soc+=count;
				soc+=vl[si];
			}
			else
				soc+=vl[si];
		}


		cout<<"Case #"<<tc++<<": "<<count;
	}
	
	return 0;
}