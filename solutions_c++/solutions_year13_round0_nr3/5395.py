#include <iostream>
#include <math.h>
using namespace std;

int su(int NN) // 자릿수 구하기.
{
	int s= 1,c = 10;
	while(NN / c)
	{
		s++;
		c *=10;
	}
	return s;
}

bool test(double NN)
{
	double TN = sqrt(NN); // 제곱근
	if(TN-(int)TN == 0) // 제곱근의 자연수 판별
	{
		int N = TN; // 제곱근 수 
		int SU = su(NN);
		if(SU==1)
			return true;
		else
		{
			char TT[1000]={0,};
			itoa(NN,TT,10);
			if(TT[0]==TT[SU-1]) //본래 수 맨 앞자리 맨 뒷자리 체크.
			{
				char TTT[1000]={0,};
				itoa(N,TTT,10);
				SU=su(N);
				if(TTT[0]==TTT[SU-1]) // 제곱근 수 맨 앞자리 맨 뒷자리 체크.
					return true;
				else
					return false;
			}
			else
				return false;
		}
	}
	else
	{
		return false;
	}
	return false;
}

int main()
{
	int T,A,B;
	int r=0;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>A>>B;
		for(;A<=B;A++)
		{
			if(test(A))
			{
				r+=1;
			}
		}
		cout<<"Case #"<<i<<": "<<r<<endl;
		r=0;
	}
}