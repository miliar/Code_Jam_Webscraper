#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
#include<vector>


using namespace std;


bool IsPalindromic(unsigned long long x)
{
	int LSD, MSD;//least and most segnificant digits
	if(x<10)
	{
		return true;
	}
	LSD = int(x%10);
	x = unsigned long long(x/10);
	int digitsCount = floor(log10(x))+1;
	unsigned long long temp = unsigned long long(pow(10,digitsCount-1));
	MSD = int(x/temp);
	x = x%temp;
	if(LSD == MSD)
		return IsPalindromic(x);
	else
		return false;
}

void Initialize(int max, vector<unsigned long long> & list)
{
	for(unsigned long long i=0; i<floor(sqrt(max)); i++)
	{
		unsigned long long ii = i*i;
		if(IsPalindromic(i) && IsPalindromic(ii))
			list.push_back(ii);
	}
}

int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	int T;
	inpFile>>T;

	vector<unsigned long long>list;
	Initialize(1000, list);

	for(int i=0; i<T; i++)
	{
		unsigned long long a, b;
		inpFile>>a>>b;
		int sum = 0;
		for(int j=0; j<list.size(); j++)
		{
			if(list[j]<a)
				continue;
			if(list[j]>b)
				break;
			sum++;
		}
		outFile<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	

	

}