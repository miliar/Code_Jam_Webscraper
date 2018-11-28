#include<iostream>
using namespace std;

int main()
{
	int T,N,mid,digit,NArray[100];
	cin >> T;
	for (int i=1;i<=T;i++)
	{
		cin >> N;
		mid = N;
		bool digitcheck[10];
		for (int m=0;m<10;m++)
			digitcheck[m]=false;
		int count(0),countTime(0);
		while (count!=10 && countTime<1000000)
		{
		 count = 0;
		 bool start(false);
		 for (int a=1000000;a>=10;a/=10)
		 {
			digit = (N%a)/(a/10);
			if (digit!=0) start=true;
			if (digit!=0) digitcheck[digit] = true;
			else if (start) digitcheck[0] = true;
		 }
		 for (int j=0;j<10;j++)
			if (digitcheck[j]==true)
				count++;
		 if (count != 10) N += mid;
		 countTime++;
		}
		if (count==10) NArray[i-1] = N;
		else NArray[i-1] = 9999999;
		
	}
	for (int i=1;i<=T;i++)
	{	
		if (NArray[i-1]!=9999999) cout << "Case #" << i << ": " << NArray[i-1] << endl;
		else cout << "Case #" << i << ": INSOMNIA" << endl;
	}
	return 0;
}

