#include<iostream>
#include<cmath>

using namespace std;

int cnt[1000001];


int isPalindrome(long n)
{
	long p=0,q=n,r=10;
	while(q)
	{
		p=p*10 + q%10;
		q/=10;
	}
	if(p==n)
		return 1;
	else
		return 0;
}

void calculatePalindromeCounts(long k)
{
	 for(long i=0;i<=k;i++)
	{
		int p=0;
		for(long j=i*10000;j<(i+1)*10000;j++)
			if(isPalindrome(j) && isPalindrome(j*j))
				p++;
		cnt[i]=p;
	}
}
			
int main()
{
	long T,A,B,i,C,D,count=0;
	cin >> T;

	//calculatePalindromeCounts(1);

	for(i=1;i<=T;i++)
	{
		cin >> A >> B;
		C=ceil(sqrt(A));
		D=floor(sqrt(B));

		count=0;
		for(int j=C;j<=D;j++)
			if(isPalindrome(j) && isPalindrome(j*j))
				count++;

		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
