#include<iostream>
#include<string>
#include<fstream>
using namespace std;

/*
1 = 1
i = 2
j = 3
k = 4
-i = 5
-j = 6
-k = 7
-1 = 8
*/

char multiply(char a, char b)
{
	if (a == b)
	{
		if (a == 1 || a==8 )
		{
			return 1;
		}
		else
		{
			return 8;
		}
	}
	else if (a == 8 || b == 8)
	{
		if (a==8)
		{
			if (b == 3 || b == 2 || b == 4)
			{
				return b + 3;
			}
			else if (b == 5 || b == 6 || b == 7)
			{
				return b - 3;
			}
		}
		else if (b == 8)
		{
			if (a == 2 || b == 3 || b == 4)
			{
				return a + 3;
			}
			else if (a == 5 || a == 6 || a == 7)
			{
				return a - 3;
			}
		}
	}
	else if (a == 1)
	{
		return b;
	}
	else if (b == 1)
	{
		return a;
	}
	else if (a == b + 3 || b==a+3)
	{
		return 1;
	}
	/*	bad programming starts here		*/
	else if (a == 2 && b == 3)
	{
		return 4;
	}
	else if (a == 2 && b == 4)
	{
		return 6;
	}
	else if (a == 2 && b == 6)
	{
		return 7;
	}
	else if (a == 2 && b == 7)
	{
		return 3;
	}
	/*2*/
	else if (a == 3 && b == 4)
	{
		return 2;
	}
	else if (a == 3 && b == 5)
	{
		return 4;
	}
	else if (a == 3 && b == 7)
	{
		return 5;
	}
	/*3*/
	else if (a == 4 && b == 5)
	{
		return 6;
	}
	else if (a == 4 && b == 6)
	{
		return 2;
	}
	/*4*/
	else if (a == 5 && b == 6)
	{
		return 4;
	}
	else if (a == 5 && b == 7)
	{
		return 6;
	}
	/*5*/
	else if (a == 6 && b == 7)
	{
		return 2;
	}
	/*6*/
	/*bad programming part 2*/
	else if (a == 3 && b == 2)
	{
		return 7;
	}
	else if (a == 4 && b == 2)
	{
		return 3;
	}
	else if (a == 6 && b == 2)
	{
		return 4;
	}
	else if (a == 7 && b == 2)
	{
		return 6;
	}
	/*2*/
	else if (a == 4 && b == 3)
	{
		return 5;
	}
	else if (a == 5 && b == 3)
	{
		return 7;
	}
	else if (a == 7 && b == 3)
	{
		return 2;
	}
	/*3*/
	else if (a == 5 && b == 4)
	{
		return 3;
	}
	else if (a == 6 && b == 4)
	{
		return 5;
	}
	/*4*/
	else if (a == 6 && b == 5)
	{
		return 7;
	}
	else if (a == 7 && b == 5)
	{
		return 3;
	}
	/*5*/
	else if (a == 7 && b == 6)
	{
		return 5;
	}
	/*6*/
}

int main()
{
	ifstream in("Small.txt");
	ofstream out("SmallC_Output.txt");
	int cases = 0;
	in >> cases;
	string *s = new string[cases];
	int *lens = new int[cases];
	int rep = 0;
	string temp;
	for (int i = 0; i < cases; i++)
	{
		in >> lens[i];
		in >> rep;
		lens[i] = lens[i] * rep;
		in >> temp;
		s[i] = temp;
		for (int j = 0; j < rep-1; j++)
		{
			s[i] = s[i] + temp;
		}
	}
	for (int i = 0; i < cases; i++)
	{
		for (int j = 0; j < lens[i]; j++)
		{
			if (s[i][j] == 'i')
			{
				s[i][j] = 2;
			}
			else if (s[i][j] == 'j')
			{
				s[i][j] = 3;
			}
			else if (s[i][j] == 'k')
			{
				s[i][j] = 4;
			}
		}
	}
	bool check = false;
	/*bullshit over, real code starts here*/
	for (int q = 0; q < cases; q++)
	{
		check = false;
		int len = lens[q];
		if (len<3)
		{
			check = false;
		}
		else if (len == 3)
		{
			if (s[q][0] == 2 && s[q][1] == 3 && s[q][2] == 4)
			{
				check = true;
			}
		}
		else
		{
			int i = 0;
			bool iflag = true;
			bool jflag = true;
			char r;
			while (len>=1)
			{
				r = multiply(s[q][i], s[q][i + 1]);
				//if (r == 1)
				//{
				//	i = i + 2;
				//	len = len - 2;
				//	//for (int j = i; j < len; j++)
				//	//{
				//	//	s[q][j] = s[q][j + 2];
				//	//}
				//	//len--;
				//	//len--;
				//}
				//else 
				if (r == 2 && iflag == true)
				{
					i++;
					i++;
					len--;
					len--;
					/*s[q][i] = r;
					i = 1;
					for (int j = i; j < len; j++)
					{
						s[q][j] = s[q][j + 1];
					}
					len--;*/
					iflag = false;
				}
				else if (r == 3 && jflag == true && iflag == false)
				{
					i++;
					i++;
					len--;
					len--;
					//s[q][i] = r;
					//i = 2;
					//for (int j = i; j < len; j++)
					//{
					//	s[q][j] = s[q][j + 1];
					//}
					//len--;
					jflag = false;
				}
				else
				{
					s[q][i + 1] = r;
					i++;
					len--;
					//for (int j = i; j < len; j++)
					//{
					//	s[q][j] = s[q][j + 1];
					//}
					//len--;
				}
			}
			if (s[q][0] == 2 && s[q][1] == 3 && s[q][2] == 4)
			{
				check = true;
			}
			else if (iflag==false && jflag==false && s[q][i]==4)
			{
				check = true;
			}
		}
		out << "Case #" << q + 1 << ": ";
		if (check == true)
		{
			out << "YES" << endl;
		}
		else
		{
			out << "NO" << endl;
		}
	}
}