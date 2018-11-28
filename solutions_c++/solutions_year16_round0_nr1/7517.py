#include <iostream>
#include <fstream>
using namespace std;


bool checkDigitCount(int digitCount[])
{
	for(int i=0;i<10;i++)
		if(digitCount[i]==0)
			return false;
	return true;
}

int main()
{
	ifstream fp("lfile1.in");
	ofstream outfp("file.out");
	int T;
	fp >> T;
	int t = 1;
	while(t<=T)
	{
		int N;
		int digitCount[10] = {0};
		fp>>N;
		int flag = 1;
		for(int i=1, M=N; flag == 1; ++i, M=N*i)
		{
			if(M==N && i>1)
			{
				outfp<<"Case #"<<t<<": INSOMNIA"<<endl;
				break;
			}
			int temp = M;
			while(temp>0)
			{
			 	int j = temp%10;
			 	digitCount[j]++;
			 	temp = temp/10;
			}
			if(checkDigitCount(digitCount))
			{
				outfp<<"Case #"<<t<<": "<<M<<endl;
				break;
			}
		}
		t++;
	}
}

