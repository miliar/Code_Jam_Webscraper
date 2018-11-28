#include<stdio.h>
#include<iostream>
//#include<conio.h>
#include<fstream>
using namespace std;
//int count;
void stack(char* str, int point)
{
	int i ;
	for (i = 0; i <= point; i++)
	{
		if (*(str+i) == '+')
			*(str+i) = '-';
		else
			*(str+i) = '+';

	}
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("int.in");
	fout.open("out.txt");
	char str[110];
	int t, len, count, i = 1;;
	//scanf("%d", &t);
	fin >> t;
	//cout << t;
	while (t--)
	{
		count = 0;
		//scanf("%s", str);
		fin >> str;
		//cout << str;
		len = strlen(str);
		while (len > 0)
		{
			len--;
			if (str[len] == '-')
			{
				count++;
				stack(str, len);
			}
			
		}
		//printf("%s\n", str);
		//printf("%d\n", count);
		fout <<"Case #"<<i<<": "<< count << endl;
		i++;
		//cout << count;
		//getch();
	}
	fin.close();
	fout.close();
}