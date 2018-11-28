#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T,N,J,count(0);
	long long limit(1),rem,quot;
	cin >> T;
	cin >> N >> J;
	cout << "Case #1:\n";
	int array[32];
	array[0]=1;
	array[N-1]=1;
	for (int i=1;i<=N-2;i++)
	{
		array[i] = 0;
		limit *= 2;
	}
	for (int i=0;i<=limit-1;i++)
	{
	  int mid(i),base(2),divisor[9];
	  for (int j=0;j<9;j++)
		 divisor[j] = 1;
	  bool judge(true);
	  for (int j=N-3;j>=1;j--)
	  {
		  quot = mid/2;
		  rem = mid%2;
		  mid = quot;
		  array[j+1] = rem;
	  }
	  array[1] = mid;
	  for (base=2;base<=10;base++)
	  {
		  long long sumInDecimal(0);
		  for (int k=0;k<N;k++)
		  {
			long long multiplier(1);
			for (int m=N-1;m>k;m--) multiplier *= base;
			sumInDecimal += array[k] * multiplier;
		  }
		  for (long long j=2;j<=sqrt(sumInDecimal);j++)
		   if (sumInDecimal%j==0) {divisor[base-2] = j;break;}
		  if (divisor[base-2] == 1) {judge = false; break;}
	  }
	  if (judge && count < J)
	  {
		for (int j=0;j<N;j++)
		 cout << array[j];
		for (int j=0;j<9;j++)
		 cout << " " << divisor[j];
		cout << endl;
		count++;
	  }  
	  if (count==J) break;
    } 
	return 0;
}


