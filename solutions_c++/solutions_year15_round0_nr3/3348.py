#include<iostream>
#include<string>

//i 2
//j 3
//k 4
using namespace std;

int a[][4] = { 1, 2, 3, 4, 2, -1, 4, -3, 3, -4, -1, 2, 4, 3, -2, -1 };

int chartoint(char ch)
{
	switch (ch)
	{
	case '1':
		return 1;
	case 'i':
		return 2;
	case 'j':
		return 3;
	case 'k':
		return 4;
	}
	return -1;
}

char inttochar(int ch)
{
	switch (ch)
	{
	case 1:
		return '1';
	case 2:
		return 'i';
	case 3:
		return 'j';
	case 4:
		return 'k';
	}

	return '-1';
}

int multiply(int m, int n)
{
	int flag=1;

    if(m<0)
    {
        flag=-1;
        m=-m;
    }

    if(n<0)
    {
        flag=flag*-1;
        m=-m;
    }

    return a[m-1][n-1]*flag;
}

void main()
{
	int T, L, X, i, len;
	string S, s;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> L >> X;
		cin >> S;
		
		s = S;
		while (--X)
			S += s;
		len = S.length();
		
		int f = 0, pro = 1;
		char next='i';
		
		for (i = 0; i < len; i++)
		{
			int temp = chartoint(S[i]);
			
			pro=multiply(pro,temp);
			
			if(inttochar(pro)==next)
			{
				f=1;
				
				if(next!='k')
				{
					next=inttochar((chartoint(next) + 2) % 3 + 2);
					pro=1;
				}
			}
			else
				f=0;
		}

		if (f == 1)
			cout << "Case #" << t << ": YES" << endl;
		else
			cout << "Case #" << t << ": NO" << endl;

	}
}
