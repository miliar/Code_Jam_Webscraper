# include <iostream>
# include <string>
# include <fstream>

using namespace std;

string dijkstraMul (string a, char temp)
{
	string b = "";
	b += temp;
	if (a == "1")
	{
		return b;
	}
	if (a == b)
	{
		return "-1";
	}
	if (a == "-1")
	{
		a = "-";
		a += b;
		return a;
	}
	if ((a == "-i" || a == "-j" || a == "-k") && b [0] == a [1])
	{
		return "1";
	}
	if (a == "i")
	{
		if (b == "j")
		{
			return "k";
		}
		else
		{
			return "-j";
		}
	}
	else if (a == "j")
	{
		if (b == "i")
		{
			return "-k";
		}
		else
		{
			return "i";
		}
	}
	else if (a == "k")
	{
		if (b == "i")
		{
			return "j";
		}
		else
		{
			return "-i";
		}
	}
	else if (a == "-i")
	{
		if (b == "j")
		{
			return "-k";
		}
		else
		{
			return "j";
		}
	}
	else if (a == "-j")
	{
		if (b == "i")
		{
			return "k";
		}
		else
		{
			return "-i";
		}
	}
	else if (a == "-k")
	{
		if (b == "i")
		{
			return "-j";
		}
		else
		{
			return "i";
		}
	}
}

bool dijkstra (int L, int X, string &temp1)
{
	string check = "", temp = "", a = "1";
	int i = 0;
	for (int j = 0; j < X; j++)
	{
		temp += temp1;
	}
	while (i < temp.length () && a != "i")
	{
		a = dijkstraMul (a, temp [i++]);
	}
	check += a;
	a = "1";
	while (i < temp.length () && a != "j")
	{
		a = dijkstraMul (a, temp [i++]);
	}
	check += a;
	a = "1";
	while (i < temp.length ())
	{
		a = dijkstraMul (a, temp [i++]);
	}
	check += a;
	if (check == "ijk")
	{
		return true;
	}
	return false;
}

int main ()
{
	int testCases, L, X;
	string temp;
	ifstream in ("C-small-attempt1.in");
	ofstream out ("C-small-attempt1.out");
	in >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		in >> L >> X;
		in >> temp;
		if (dijkstra (L, X, temp))
		{
			out << "Case #" << i+1 << ": YES\n";
		}
		else
		{
			out << "Case #" << i+1 << ": NO\n";
		}
		temp = "";
	}
	in.close ();
	out.close ();

	return 0;
}