#include<iostream>
#include<stdio.h>

using namespace std;

template <class number>
void mergesort(number A[], number p, number q)
{
	if(p == q)
		return;
	number r = (p + q) / 2;
	
	mergesort(A, p, r);
	mergesort(A, r + 1, q);
	
	number l = q - p + 1;
	number *a = new number[l];
	
	number m1 = 0, m2 = r - p + 1;
	for(int i = 0; i < l; i++)
	{
		a[i] = A[p+i];
	}	
	
	for(int i = p; i <= q; i++)
	{
		if(p + m1 > r)
		{
			A[i] = a[m2++];
		}
		else if(p + m2 > q)
		{
			A[i] = a[m1++];
		}
		else if(a[m1] < a[m2])
			A[i] = a[m1++];
		else
		{
			A[i] = a[m2++];
		}
	}	
}

int main(void)
{
	freopen("C:/Downloads/A-Large.in", "r", stdin);
	freopen("C:/Downloads/A-Large.out", "w+", stdout);
	int T, num;
	cin>>T;
	int n = 1;
	long int A, N;
	long int motes[101];
	long int count[101] = {0};
	long int current_size;
	while(T--)
	{
		cin>>A>>N;
		for(int i = 0; i < N; i++)
		{
			cin>>motes[i];
			count[i] = 0;
		}
		
		mergesort(motes, (long int)0, N-1);
		
		num = 0;
		current_size = A;
		for(int i = 0; i < N; i++)
		{
			while(current_size <= motes[i])
			{
				if(current_size == 1)
				{
					num++;
					break;
				}
				current_size += (current_size-1);
				num++;
				count[i]++;
			}
			if(current_size > motes[i])
			current_size += motes[i];
		}
		
		for(int i = N-1; i >= 0; i--)
		{
			if(count[i] >= (N-i))
			{
				num -= count[i];
				num += (N - i);
				N = i;
			}
		}
		
		cout<<"Case #"<<n++<<": "<<num<<endl;
	}
}
