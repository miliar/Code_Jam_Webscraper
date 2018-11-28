#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int findMax(int * n, int x, int *in)
{
	int max = n[0];
	*(in) = 0;

	for (int i = 1; i < x; i++)
	{
		if (max < n[i])
		{
			max = n[i];
			*(in) = i;
		}
	}

	return max;
}

int main()
{
	/*int a[10] = {6,2,8,1,0,4,7,3,9,5};
	int tmp,i,j;

	for (i = 1; i<10; i++)
	{
		tmp = a[i];

		for (j = i - 1; j > 0; j--)
		{
			if (a[j] > tmp)
			{
				a[j + 1] = a[j];
			}
			else
				break;
		}

		a[j + 1] = tmp;

	}


	cout << a[7] << "  " << a[8] << "  " << a[9] << "  " << endl;*/


	ofstream out("output.txt");
	ifstream in("B-large.in");
	int k,  ans, tmp, r, *n,x;
	string num, name;
	bool ch = true;
	in >> k;

	for (int j1 = 0; j1 < k; j1++)
	{
		ch = true;
		tmp = 0;
		ans = 0;
		in >> x;

		n = new int[x];

		for (int i = 0; i < x; i++)
		{
			in >> n[i];
		}
		
		int index;

		ans = 0;
		int min1, max1,sum;

		
			max1 = findMax(n,x,&r);

		min1 = max1;
		for (int i = 1; i <= max1; i++) {
			sum = i;
			for (int j = 0; j < x; j++) {
				if (n[j] > i) {
					if (n[j] % i == 0)
						sum += (n[j] / i - 1);
					else
						sum += (n[j] / i);
				}
			}
			
			if (min1 > sum)
				min1 = sum;
		}

		/*while (ch)
		{
			int max = findMax(n, x, &index);

			if (max > 2 && (max % 2) != 0)
			{
				int * tmp = new int[++x];

				for (int i = 0; i < x - 1; i++)
				{
					if (i == index)
						tmp[i] = n[i] - (n[i] / 2);
					else
						tmp[i] = n[i];
				}

				tmp[x - 1] = (n[index] / 2);

				n = new int[x];

				for (int i = 0; i < x; i++)
				{
					n[i] = tmp[i];
				}

				ans++;
			}
			
			for (int i = 0; i < x; i++)
			{
				n[i] = n[i] - 1;
			}

			ans++;

			for (int i = 0; i < x; i++)
			{
				if (n[i] > 0)
				{
					ch = true;
					break;
				}
				else
					ch = false;
			}
		}*/
		

		out << "Case #" << j1 + 1 << ": " << min1 << endl;
	}
	

	return 0;
}


//1
/*ofstream out("output.txt");
ifstream in("A-small-attempt.in");
int n, m, ans, tmp;
string num;
in >> n;

for (int j = 0; j < n; j++)
{
	tmp = 0;
	ans = 0;
	in >> m;
	in >> num;


	for (int i = 1; i < num.length(); i++)
	{
		tmp += num[i - 1] - 48;

		if (tmp < i)
		{
			ans += i - tmp;
			tmp += i - tmp;
		}
	}


	cout << "Case #" << j + 1 << ": " << ans << endl;
}*/