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
	
	int arr[10];
	int i,fact,rem,count=0;
	long N,tmp,ans;
	bool flg=true;

	cin>>N;

	bool itrFlg = false;
	int tc=1;
	while(run--)
	{
		if(itrFlg)
		{
			flg=true;
			count=0;
			cout<<endl;
			cin>>N;
		}
		itrFlg = true;
		//Check for the existence of other Boundary Conditions. 
		if(N==0)
		{
			cout<<"Case #"<<tc++<<": "<<"INSOMNIA";
			continue;
		}
		//initialize arr
		for(i=0;i<10;i++)
			arr[i]=-1;

		i=1;
		tmp=N;
		while(flg)
		{
			ans=tmp;
			fact=0;
			rem=0;
			while(tmp>0)
			{
				rem=tmp%10;
				tmp=tmp/10;
				
				if(arr[rem]!=rem)
				{
					arr[rem]=rem;
					count++;
				}
				if(count==10)
				{
					flg=false;
					continue;
				}
			}
			tmp=N*(++i);
		}

		cout<<"Case #"<<tc++<<": "<<ans;
	}
	
	return 0;
}