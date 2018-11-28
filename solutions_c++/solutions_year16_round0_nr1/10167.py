#include<bits/stdc++.h>
using namespace std;

int main(void)
{
	int t, k;
	long long n, copy, i, solid;
	int num[10], x, count;
	ifstream in;
	ofstream out;
	in.open("input");
	out.open("output");
	in >> t;
	for(k=1; k<=t; k++)
	{
		memset(num, 0, sizeof(num));
		in >> n;
		if(n == 0)
			out << "Case #" << k << ": " << "INSOMNIA" << endl;
		else
		{
			for(i=1; ; i++)
			{
				solid = i*n;
				copy = i*n;
				while(copy)
				{
					num[copy%10] = 1;
					count = 0;
					for(x=0; x<10; x++)
						if(num[x] == 1)
							count++;
					if(count == 10)
						goto out;
					copy = copy/10;
				}
			}
out:
			out << "Case #" << k << ": " << solid << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}
