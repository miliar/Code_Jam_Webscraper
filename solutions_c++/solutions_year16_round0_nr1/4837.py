
#include <iostream>
#include <string>

using namespace std;

int numbers[10];

int length(int number)
{    
      int counter=0;
      while(number)
     {        
            number=number/10;
            counter++;
      }
      return (counter);
}

int check()
{
	for(int i = 0; i < 10; i++)
		if(numbers[i] == 0)
			return 0;
			
	return 1;
}

void add(int i)
{
	numbers[i] = 1;	
}

int main()
{
	for(int i = 0; i < 10; i++)
		numbers[i] = 0;
	
	int T;
	int result;
	int j;
	int k;
	char c;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		for(k = 1; ; k++)
		{
			if(N==0)
				break;
			int base = 1;
			for(j = 0; j < length(N*k); j++)
			{
				int num;
				num = (N*k) / base % 10;
				add(num);
				base = base*10;	
			}
			if(check())
				break;
		}
		cout << "Case #" << t << ": ";
		if(N!=0)
			cout << k*N << endl;
		else
			cout << "INSOMNIA" <<endl;
		for(int i = 0; i < 10; i++)
			numbers[i] = 0;
	}
	

	return 0;
}


