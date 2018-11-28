#include <stdio.h>


void next_permu(int* arr, int len);

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
	int T;
	int N, J;

	int threshold;

	int poly_odd[20];
	int poly_even[20];
	int len_odd, len_even;
	int w_odd, w_even;
	bool flag, toggle;

	scanf("%d", &T);
	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%d %d", &N, &J);

		printf("Case #%d:\n", test_case);

		w_odd = w_even = 0;
		len_odd = (N-1)/2;
		len_even = (N-2)/2;
		for(int i=0;i<len_odd;i++)	poly_odd[i] = 0;
		for(int i=0;i<len_even;i++)	poly_even[i] = 0;

		if(N%2==1)
		{
			w_odd = 2;
			poly_even[0] = poly_even[1] = 1;
		}

		while(J>0)
		{
			if(N%2==1) toggle = true;
			else	   toggle = false;

			printf("1");
			for(int i=0;i<N-2;i++)
			{
				if(toggle)
					printf("%d", poly_odd[i/2]);
				else
					printf("%d", poly_even[i/2]);

				toggle = !toggle;
			}
			printf("1");

			for(int i=2;i<=10;i++)
				printf(" %d", i+1);
			printf("\n");
			J--;

			// generate next
			flag = false;
			for(int i=0;i<len_even-1;i++)
			{
				if(poly_even[i]==1 && poly_even[i+1]==0)
					flag = true;	
			}
			if(flag==false)
			{
				for(int i=0;i<len_odd-1;i++)
				{
					if(poly_odd[i]==1 && poly_odd[i+1]==0)
						flag = true;
				}
				if(flag==false)
				{
					w_odd++; w_even++;
					for(int i=0;i<w_odd;i++)		 poly_odd[i] = 1;
					for(int i=w_odd;i<len_odd;i++)	 poly_odd[i] = 0;

					for(int i=0;i<w_even;i++)		 poly_even[i] = 1;
					for(int i=w_even;i<len_even;i++) poly_even[i] = 0;	
				}
				else
				{
					next_permu(poly_odd, len_odd);
					for(int i=0;i<w_even;i++)		 poly_even[i] = 1;
					for(int i=w_even;i<len_even;i++) poly_even[i] = 0;
				}
			}
			else
			{
				next_permu(poly_even, len_even);
			}
		}
	}

	return 0;
}

void next_permu(int *arr, int len)
{
	int offset=0;
	for(int i=len-1;i>=0;i--)
	{
		if(arr[i]==1)
			offset++;
		else
			break;
	}
	for(int i=len-1;i>=0;i--)
	{
		if(arr[i-1]==1 && arr[i]==0)
		{
			arr[i-1]=0; arr[i] = 1;
			for(int j=i+1;j<i+1+offset;j++)
				arr[j] = 1;
			for(int j=i+1+offset;j<len;j++)
				arr[j] = 0;
			break;
		}
	}
}