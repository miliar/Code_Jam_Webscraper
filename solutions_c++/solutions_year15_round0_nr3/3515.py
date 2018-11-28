// Google3.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int condition(int a, int b);

int main(void)
{
	int total;

	scanf("%d", &total);

	const int size = total;

	char *srr = (char*)malloc(total);

	int index = 0;
	
	int i;
	
	char flag;

	int q, r;

	char oi, oj, ok;

	int t_sum;

	while (total--)
	{
		scanf("%d %d\n", &q, &r);

		char *str = (char*)malloc(q + 1);

		
		fgets(str, q + 1, stdin);


		int *test = (int*)malloc(sizeof(int)*q);
		
		flag = 1;
	
		char *check = (char*)malloc(3);

		memset(check, 0, 3);

		t_sum = 0;

		int n1, n2;

		for (i = 0; i < q; i++) //비용이 많이 들 가능성이 존재한다. 어쩌라고 진짜
		{
			if (str[i] == 'i')
			{
				test[i] = 2;
				check[0] = 1;
			}

			if (str[i] == 'j')
			{
				test[i] = 3;
				check[1] = 1;
			}

			if (str[i] == 'k')
			{
				test[i] = 4;
				check[2] = 1;
			}
		}
	    
		if (q*r < 3)
		{
			flag = 0;
		}
		
		for (i = 0; i < 3; i++)
		{
			t_sum += check[i];
		}

		if (t_sum == 1)
		{
			flag = 0;
		}

		if (flag == 1) 
		{
			int xb = 2;
			
			r--;

			i = 0;

			n1 = test[i++];
			
			char is = false;

			while (n1 == xb && r >= 0)
			{
				
				n1 = test[i++];
				xb++;

				if (i == q)
				{
					i = 0;
					r--;
				}

				if (xb == 4)
				{
					is = true;
					break;
				}
			}
			
			if (is == false)
			{
				n2 = test[i++];

				if (i == q)
				{
					i = 0;
					r--;
				}

				while (r >= 0)
				{
					n1 = condition(n1, n2);

					n2 = test[i];

					if (n1 == xb)
					{
						if (xb == 4)
						{
							break;
						}

						xb++;

						n1 = n2;
						i++;

						if (i == q)
						{
							i = 0;
							r--;
						}

						n2 = test[i++];

						if (i == q)
						{
							i = 0;
							r--;
						}
						continue;
					}


					i++;
					if (i == q)
					{
						i = 0;
						r--;
					}
				}


				//여기서 r이 몇번째고 i가 몇번째 인지 알수가 있다.
				if (r < 0)
				{
					n1 = condition(n1, n2);
				}

			}
				if (n1 != 4)
				{
					flag = 0;
				}

				if (flag != 0)
				{
					if (r >= 0)
					{	
						n1 = test[i++];

						if (i == q)
						{
							i = 0;
							r--;
						}

						if (r < 0)
						{
							if (condition(4, n1) != 4)
							{
								flag = 0;
							}
						}

						n2 = test[i++];
						
						if (i == q)
						{
							i = 0;
							r--;
						}
						
						while (r >= 0)
						{
							n1 = condition(n1, n2);
							n2 = test[i];

							i++;
							if (i == q)
							{
								i = 0;
								r--;
							}
						}

						n1 = condition(n1, n2);

						
						if (condition(4, n1) != 4)
						{
							flag = 0;
						}
					}
				}
			
     }
		
		srr[index] = flag;
		index++;
	}   
	
	for (i = 0; i < size; i++)
	{
		if (srr[i] == 0)
		{
			printf("Case #%d: No\n",i+1);
		}
		else
		{
			printf("Case #%d: Yes\n", i + 1);
		}
	}

	return 0;
}


int condition(int a, int b)
{
	int arr[4][4]=
	{
		{ 1, 2, 3, 4 },
		{ 2, -1, 4, -3 },
		{3,-4,-1,2},
		{4,3,-2,-1}
	};

	if (a < 0 && b<0)
	{
		return arr[-a-1][-b-1];
	}
	if (a < 0)
	{
		return arr[-a-1][b-1] * -1;
	}
	
	if (b < 0)
	{
		return arr[a-1][-b-1] * -1;
	}
	return arr[a-1][b-1];

}