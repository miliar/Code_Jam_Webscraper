#include <iostream>
#include <fstream>
#include <string>

int getNValue(int n, std::string name)
{
	//std::cout<<"start\n";
	if(n<1)
	{
		return -1;//control value for failure
	}
	if(name.size()<n)
		return 0;
	bool *bArr;
	bArr=new bool[name.size()];
	for(int i=0;i<name.size();++i)
	{
		bArr[i]=!(name[i]=='a'||name[i]=='e'||name[i]=='i'||name[i]=='o'||name[i]=='u');
		//std::cout<<bArr[i];
	}
	//std::cout<<'\n';
	int count=0;
	int j=0;
	int out=0;
	for(int i=0;i<name.size();++i)
	{
		count=0;
		j=i;
		//std::cout<<"start while\n";
		while(count<n&&j<name.size())
		{
			if(bArr[j])
			{
				++count;
				//std::cout<<j<<'\n';
				//std::cout<<count<<'\n';
			}
			else
			{
				count=0;
			}
			//std::cout<<j<<' '<<bArr[j]<<' '<<count<<'\n';
			++j;
		}
		//std::cout<<"j="<<j<<'\n';
		out+=name.size()-j;
		if(!(count<n))
		{
			++out;
		}
		//std::cout<<i<<' '<<out<<"currval\n";
		
	}
	return out;
}
int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		std::cerr<<"Improper call\n";
		return 1;
	}
	std::ifstream inFile(argv[1]);
	std::ofstream outFile(argv[2]);
	if(!inFile)
	{
		std::cerr<<"infile incorrectly typed or nonexistent\n";
		return 2;
	}

	int cases=0;
	inFile>>cases;
	int n;
	std::string name;
	for(int i=0;i<cases;++i)
	{
		inFile>>name;
		inFile>>n;
		//std::cout<<name<<'\n';
		//std::cout<<n<<'\n';
		outFile<<"Case #"<<i+1<<": "<<getNValue(n, name)<<'\n';
	}
	outFile.close();
	return 0;//normal exit
}