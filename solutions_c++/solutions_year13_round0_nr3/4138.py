#include<fstream>
#include<string.h>
#include<stdio.h>
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");
__int64 Data[40] = {1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};

/*int ispalin(__int64 a)
{
	char Temp[20]={0,};

	sprintf(Temp,"%lld",a);

	int len = strlen(Temp);

	int i;
	for(i=0;i<(len/2)+1;i++)
	{
		if(Temp[i] != Temp[len-i-1])return 0;
	}
	return 1;
}*/
int main()
{
	int T;
	in>>T;
	for(int t=0;t<T;t++)
	{
		__int64 i,j;
		__int64 n, m;
		int ans=0;
		in >> n >> m;
		for(i=0;i<=38;i++)
		{
			__int64 a = Data[i]*Data[i];
			if( a >= n && a <= m)ans++;
		}
		out << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}