#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

enum value { NONE, ONE, I, J, K, NI, NJ, NK, NO};

value multiply(value x, value y)
{
	int negatives = 0;
	if(x == NONE)
	{
		negatives++;
		x = ONE;
	}
	if(x == NI)
	{
		negatives++;
		x = I;
	}
	if(x == NJ)
	{
		negatives++;
		x = J;
	}
	if(x == NK)
	{
		negatives++;
		x = K;
	}

	if(y == NONE)
	{
		negatives++;
		y = ONE;
	}
	if(y == NI)
	{
		negatives++;
		y = I;
	}
	if(y == NJ)
	{
		negatives++;
		y = J;
	}
	if(y == NK)
	{
		negatives++;
		y = K;
	}

	value answer = x;

	if(x == ONE)
	{
		answer = y;
	}
	else if(x == I)
	{
		switch(y)
		{
		case ONE:	answer = I;	break;
		case I:		answer = ONE;	negatives++;	break;
		case J:		answer = K;	break;
		case K:		answer = J;		negatives++;	break;
		}
	}
	else if(x == J)
	{
		switch(y)
		{
		case ONE:	answer = J;	break;
		case I:		answer = K;		negatives++;	break;
		case J:		answer = ONE;	negatives++;	break;
		case K:		answer = I;	break;
		}
	}
	else if(x == K)
	{
		switch(y)
		{
		case ONE:	answer = K;	break;
		case I:		answer = J;	break;
		case J:		answer = I;			negatives++;	break;
		case K:		answer = ONE;		negatives++;	break;
		}
	}


	negatives %= 2;

	if(negatives)
	{
		if(answer == ONE)
		{
			answer = NONE;
		}
		if(answer == I)
		{
			answer = NI;
		}
		if(answer == J)
		{
			answer = NJ;
		}
		if(answer == K)
		{
			answer = NK;
		}
	}

	return answer;
}

int main()
{
	int tests;
	cin >> tests;

	for(int a=0; a<tests; a++)
	{
		string answer = "NO";

		int len, mul;
		cin >> len >> mul;
		string input;
		cin >> input;

		vector<value> data(len*mul);
		for(int i=0; i<input.size(); i++)
		{
			switch(input[i])
			{
			case 'i':		data[i] = I;		break;
			case 'j':		data[i] = J;		break;
			case 'k':		data[i] = K;		break;
			}
			for(int j=1; j<mul; j++)
			{
				data[i + (j * len)] = data[i];
			}
		}

		vector<value> memo(10001, NO);


		value left = ONE;
		for(int i=0; i<data.size(); i++)
		{
			left = multiply(left, data[i]);
			if(left != I)
			{
				continue;
			}
			value middle = ONE;
			for(int j=i+1; j<data.size(); j++)
			{
				middle = multiply(middle, data[j]);
				if(middle != J)
				{
					continue;
				}
				value last = ONE;
				if(memo[j+1] == NO)
				{
					for(int k=j+1; k<data.size(); k++)
					{
						last = multiply(last, data[k]);
					}
					memo[j+1]= last;
				}
				else
				{
					last = memo[j+1];
				}
				if(last == K)
				{
					answer = "YES";
					i = data.size();
					j = data.size();
					break;
				}
			}
		}

		cout << "Case #" << (a+1) << ": " << answer << endl;
	}

	return 0;
}