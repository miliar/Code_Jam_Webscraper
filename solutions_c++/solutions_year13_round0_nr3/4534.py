#include<iostream>
#include<math.h>

using namespace std;

long long nextPallin(long long  x)
{
	int size;
	long long temp = x;
	if(x == 9)
	{
		x = 11;
		return x;
	}
	if(x < 10)
	{
		x ++;
		if(x < 10)
		return x;
	}
	for(size = 0 ; temp>0 ; temp/=10 , size++);
	
	long long right = x%(long long)(pow(10,(int)(size/2)));
	long long left = x/(pow(10,(int)((size+1)/2)));
	
	left ++;
	temp = left;
	
	long long revLeft = 0;
		
	for(int i=size ; i>(size+1)/2 ; i--)
	{
		revLeft = revLeft * 10 + temp % 10;
		temp /= 10;
	}
	return (left * pow(10,size/2)+revLeft);
}
bool isPallin(long long x)
{
	long long temp = x;
	int size;
	
	for(size = 0 ; temp>0 ; temp/=10 , size++);
	
	temp = x;
	
	long long right = x%(long long)(pow(10,(int)(size/2)));
	long long left = x/(pow(10,(int)((size+1)/2)));
	long long revLeft = 0;
	
	for(int i=size ; i>(size+1)/2 ; i--)
	{
		revLeft=revLeft*10+left%10;
		left/=10;
	}
	if(revLeft == right)
		return true;
	else
	return false;
	
}
int main()
{
	int cases;
	cin >> cases;
	for(int q=0 ; q<cases ; q++)
	{
		long long A, B;
		cin >> A >> B;
		long long sqrtA, sqrtB;	
		sqrtA = (long long)(sqrt(A)+0.99999999);
		sqrtB = sqrt(B);
		long long temp = sqrtA;
		int count = 0;
		if(!isPallin(sqrtA))
		{
			int size;
			for(size = 0 ; temp>0 ; temp/=10 , size++);
			long long right = sqrtA % (long long)(pow(10,(int)(size/2)));
			long long left = sqrtA / (pow(10,(int)((size+1)/2)));
			
			long long revLeft = 0;
			if(left < right)
				left ++;
				temp = left;
				for(int i=size ; i > (size+1)/2 ; i--)
				{
					revLeft = revLeft * 10 + temp % 10;
					temp /= 10;
				}
				sqrtA = left * pow(10,size/2) + revLeft;
		}

		long long i = sqrtA;;
		while( i <= sqrtB )
		{
			if(isPallin(pow(i,2)))
			{
				count ++;
			}
			i = nextPallin(i);
		}
		cout << "Case #" << q+1 << ": " << count << "\n";		
	}
	return 0;
}
