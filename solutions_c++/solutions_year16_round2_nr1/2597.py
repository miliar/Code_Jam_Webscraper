#include <iostream>
#include <string>

void printPhone(std::string &input)
{
	unsigned e = 0, f = 0, g = 0, h = 0, i = 0, n = 0, o = 0, r = 0, s = 0, t = 0, w = 0, u = 0, v = 0, x = 0, z = 0;
	for (auto c : input)
	{
		if (c == 'E') e++;
		else if (c == 'F') f++;
		else if (c == 'G') g++;
		else if (c == 'H') h++;
		else if (c == 'I') i++;
		else if (c == 'N') n++;
		else if (c == 'O') o++;
		else if (c == 'R') r++;
		else if (c == 'S') s++;
		else if (c == 'T') t++;
		else if (c == 'W') w++;
		else if (c == 'U') u++;
		else if (c == 'V') v++;
		else if (c == 'X') x++;
		else if (c == 'Z') z++;
	}
	unsigned tab[10] = { 0 };
	while (z && e && r && o)
	{
		tab[0]++;
		z--, e--, r--, o--;
	}
	while (s && i && x)
	{
		tab[6]++;
		s--, i--, x--;
	}
	while (s && e>1 && v && n)
	{
		tab[7]++;
		s--, e--, v--, e--, n--;
	}
	while (f && i && v && e)
	{
		tab[5]++;
		f--, i--, v--, e--;
	}
	while (f && o && u && r)
	{
		tab[4]++;
		f--, o--, u--, r--;
	}
	while (t && h && r && e>1)
	{
		tab[3]++;
		t--, h--, r--, e--, e--;
	}
	while (t && w && o)
	{
		tab[2]++;
		t--, w--, o--;
	}
	while (o && n && e)
	{
		tab[1]++;
		o--, n--, e--;
	}
	while (n > 1 && i && e)
	{
		tab[9]++;
		n--, i--, n--, e--;
	}
	while (e && i && g && h && t)
	{
		tab[8]++;
		e--, i--, g--, h--, t--;
	}
	for (unsigned i = 0; i < 10; ++i)
	{
		for (unsigned j = tab[i]; j > 0; --j)
		{
			std::cout << i;
		}
	}
}

int main()
{
	unsigned tasksAmount = 0;
	std::cin >> tasksAmount;

	for (unsigned i = 1; i <= tasksAmount; ++i)
	{
		std::string input;
		std::cin >> input;
		std::cout << "Case #" << i <<": ";
		printPhone(input);
		std::cout << std::endl;
	}

    return 0;
}

