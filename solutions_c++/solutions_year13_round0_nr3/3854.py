#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>

using namespace std;

string addition(string, string);
string substraction(string, string);
int comparison(string, string);
string multiplication(string, string);

ifstream input ("input.txt");
ofstream output ("output.txt");

string powerof10(int a)
{
	string str = "";
	int i = 0;
	for(;i < a;i++)
	{
		str += "0";
	}
	str[0] = '1';
	str[i-1] = '1';
	return str;
}

bool checkpal(string num)
{
	int size = num.size();
	for(int i = 0;i < size/2;i++)
	{
		if(num[i] != num[size-i-1]) return false;
	}
	return true;
}

string numbers()
{
	string num1, num2, answer = "0";
	string A, B;
	input >> A >> B;
	num1 = powerof10(A.size()/2);
	for(;comparison(multiplication(num1, num1), B) != 1;num1 = addition(num1, "1"))
	{
		if(checkpal(num1))
		{
			if(comparison(multiplication(num1, num1), B) != 1 && comparison(multiplication(num1, num1), A) != -1 && checkpal(multiplication(num1, num1)))
			answer = addition(answer, "1");
		}
	}
	return answer;

}

int main()
{
    int T;
    input >> T;
    for(int i = 1;i <= T;i++)
    {
    	output << "Case #" << i << ": " << numbers() << endl;
    }
    return 0;
}
string addition(string a, string b)
{
	string ans;
	char memory = 48;
	char temp;

	long long sizea = a.size();
	long long sizeb = b.size();

	for(long long loopcount = 1;loopcount <= sizeb||loopcount <= sizea;loopcount++)
	{
		temp = 0;
		if(loopcount <= sizeb)
		temp += b[sizeb-loopcount]-48;
		if(loopcount <= sizea)
		temp += a[sizea-loopcount]-48;

		temp += memory-48;


		if(temp > 9)
		{
			temp = temp-10;
			memory = 49;
		}
		else
		{
			memory = 48;
		}
		temp += 48;
		ans = temp+ans;
	}
	if(memory==49)
	ans = '1'+ans;

	return ans;
}

string substraction(string a, string b)
{
	for(;;)
	{
		if(a[0] == '0') a = a.substr(1);
		else if(b[0] == '0') b = b.substr(1);
		else break;
	}
	string ans;
	char memory = 48;
	char temp;

	long long sizea = a.size();
	long long sizeb = b.size();

	if(a[0] == '-') //first is negative
	{
		if(b[0] == '-') //second is negative
		{
			return substraction(b.substr(1),a.substr(1));
		}
		else //second is positive
		{
			return "-" + addition(a.substr(1), b);
		}
	}
	else //first is positive
	{
		if(b[0] == '-') //second is negative
		{
			return addition(a, b.substr(1));
		}
		else //second is positive
		{
			if (comparison(a,b) == -1)
			{
				return "-" + substraction(b,a);
			}
			else if(comparison(a,b) == 0) return "0";
			else
			{
				for(long long loopcount = 1;loopcount <= sizeb||loopcount <= sizea;loopcount++)
				{
					temp = 0;
					if(loopcount <= sizea)
					temp += a[sizea-loopcount]-48;
					if(loopcount <= sizeb)
					temp -= b[sizeb-loopcount]-48;

					temp -= memory - 48;

					if(temp < 0)
					{
						temp += 10;
						memory = 49;
					}
					else
					{
						memory = 48;
					}
					temp +=48;
					ans = temp+ans;
				}
				if(ans[0] == '0')
				ans = ans.substr(1);
			}
		}
	}
	return ans;
}

int comparison(string a, string b) //-1, if second is bigger, 1 if first, 0 if even
{
	if(a[0] == '-') //first is negative
	{
		if(b[0] == '-') //second is negative
		{
			return -1*comparison(a.substr(1), b.substr(1));
		}
		else //second is positive
		{
			return -1;
		}
	}
	else //first is positive
	{
		if(b[0] == '-') //second is negative
		{
			return 1;
		}
		else //second is positive
		{
			long long sizea = a.size();
			long long sizeb = b.size();
			if(sizea > sizeb)
			{
				return 1;
			}
			else if(sizea < sizeb)
			{
				return -1;
			}

			for(long long loopcount = 0;loopcount < sizea;loopcount++)
			{
				if(a[loopcount]>b[loopcount])
				{
					return 1;
				}
				else if(a[loopcount] < b[loopcount])
				{
					return -1;
				}
			}
			return 0;
		}
	}
}

string multiplication(string a, string b)
{
	if(a == "0"||b == "0") //if any is 0
	{
		return "0";
	}
	if(a[0] == '-') //first negative
	{
		if(b[0] == '-') //second negative
		{
			return multiplication(a.substr(1), b.substr(1));
		}
		else //second positive
		{
			return "-"+multiplication(a.substr(1), b);
		}
	}
	else //first positive
	{
		if(b[0] == '-') //second negative
		{
			return "-"+multiplication(a, b.substr(1));
		}
		else //second positive
		{
			string ans = "0";
			string tarp;
			int tarp2;
			long long sizea = a.size();
			long long sizeb = b.size();

			for(long long loopcount = 0;loopcount < sizea;loopcount++)
			{
				for(long long loopcount2 = 0;loopcount2 < sizeb;loopcount2++)
				{
					tarp = "";
					tarp2 = (a[loopcount]-48)*(b[loopcount2]-48);
					if((tarp2/10)!=0)
					tarp +=(tarp2/10)+48;
					tarp +=(tarp2%10)+48;
					for(int loopcount3 = 0;(sizea-loopcount-1+sizeb-loopcount2-1) > loopcount3;loopcount3++) tarp += '0';
					ans = addition(ans, tarp);
				}
			}
			return ans;
		}
	}
}
