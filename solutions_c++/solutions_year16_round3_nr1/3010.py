#include<stdio.h>

int main()
{
	long long t,c;
	FILE* infp;
	FILE* outfp;
	freopen_s(&infp, "input.txt", "r", stdin);
	freopen_s(&outfp, "output.txt", "w", stdout);
	scanf_s("%lld", &t);

	for (c = 0; c < t; c++)
	{
		long long n,i;
		int p[1001];
		//Heap
		int Value[1001];
		int Party[1001];
		int Size=0;
		int index=0;
		int left = 0;
		char output[26001];
		int exist = 0;

		scanf_s("%lld", &n);

		for (i=0;i<n;i++)
		{
			scanf_s("%d", &Value[Size]);
			Party[Size] = Size;
			index = Size;
			exist += Value[Size];
			Size++;
			while(Value[(index - 1) / 2]<Value[index])
			{
				int temp1 = Value[(index - 1) / 2];
				int temp2 = Party[(index - 1) / 2];
				Value[(index - 1) / 2] = Value[index];
				Party[(index - 1) / 2] = Party[index];
				Value[index] = temp1;
				Party[index] = temp2;
				index /= 2;
			}
		}

		left = 0;

		int cut=0;
		while (Size)
		{
			Value[0]--;
			output[left]='A'+Party[0];
			left++;
			cut++;
			exist--;
			if(Value[0]==0)
			{
				int temp1 = Value[0];
				int temp2 = Party[0];
				Value[0] = Value[left];
				Party[0] = Party[left];
				Value[left] = temp1;
				Party[left] = temp2;
				Size--;
			}

			index = 0;
			while (1)
			{
				if (index * 2 >= Size 
					|| 
					(Value[(index) * 2 + 1] <= Value[index] && Value[(index ) * 2 + 2] <= Value[index])
					)
					break;

				if (Value[(index)* 2 + 1] > Value[index])
				{
					int temp1 = Value[(index)* 2 + 1];
					int temp2 = Party[(index)* 2 + 1];
					Value[(index)* 2 + 1] = Value[index];
					Party[(index)* 2 + 1] = Party[index];
					Value[index] = temp1;
					Party[index] = temp2;
					index = (index)* 2 + 1;
				}

				if (Value[(index)* 2 + 2] > Value[index])
				{
					int temp1 = Value[(index)* 2 + 2];
					int temp2 = Party[(index)* 2 + 2];
					Value[(index)* 2 + 2] = Value[index];
					Party[(index)* 2 + 2] = Party[index];
					Value[index] = temp1;
					Party[index] = temp2;
					index = (index)* 2 + 2;
				}
			}

			if (cut == 2)
			{
				if (exist < 2 * Value[0])
				{
					output[left] = output[left-1];
					output[left - 1] = ' ';
					left++;
					cut = 0;
				}
				else
				{
					output[left] = ' ';
					left++;
					cut = 0;
				}
			}

		}
		output[left] = 0;
		printf("Case #%lld: ", c + 1);
		printf("%s\n", output);
	}
	return 0;
}