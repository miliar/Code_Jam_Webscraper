#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;

bool isTheOne[1025];
int cumulative[1025];

char *strrev(char *str)
{
	int length = strlen(str);
	char *str2 = (char *)malloc(length * sizeof(char));
	for(int i = 0; i < length; i++)
		str2[length - i - 1] = str[i];
	return str2;
}

bool isPal(int num)
{
	char *str = (char *)malloc(5 * sizeof(char));
	sprintf(str, "%d", num);
	//itoa(num, str, 10);
	if(strcmp(str, strrev(str)) == 0)
		return true;
	return false;
}

void preprocess()
{
	for(int i = 0; i < 1025; i++)
		isTheOne[i] = false;
	for(int i = 1; i <= 32; i++)
	{
		if(isPal(i))
			if(isPal(i*i))
				isTheOne[i*i] = true;
	}
	
	int sum = 0;
	for(int i = 0; i < 1025; i++)
	{
		if(isTheOne[i])
		{
			//cout << i << endl;
			sum++;
		}
		cumulative[i] = sum;
	}
}

int main()
{
	int cases;
	cin >> cases;
	
	preprocess();
	
	for(int t = 1; t <= cases; t++)
	{
		int A, B;
		cin >> A >> B;
		
		cout << "Case #" << t << ": " << (cumulative[B] - cumulative[A - 1]) << endl;
	}
	
	return 0;
}
