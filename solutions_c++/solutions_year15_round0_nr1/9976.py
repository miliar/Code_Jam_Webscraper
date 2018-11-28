#include <stdio.h>
#include <conio.h>
#include <climits>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solution(string in, int n)
{
	int curr, sum=0, ans = 0;
	vector<int> shyness;
	char b = '/0';// = in.at(0);
	for(int i=0; i<=n; i++)
	{
		//char* c = in[i];
		//curr = atoi(c);
		//int a = pow(10.0, n);
		//curr = in / a;
		b = in.at(i);
		curr = atoi(&b);
		//in = in % a;
		shyness.push_back(curr);
		if(sum >= i)
		{
			ans = ans;
			sum = sum +curr;
		}
		else if(curr != 0)
		{
				ans = ans +( i - sum);
				sum = sum +curr+ ans;
		}
	}
	return ans;
}

int main()
{

	unsigned short int testcases, length;
	const char* input;
	char* A;
    cin >> testcases;
	string c;
	
    for(int i=1; i <= testcases; i++) 
	{ 
		cin >> length;
		//input = (const char *) malloc (sizeof(char)*length);
		//A = (char*) malloc (sizeof(char)*length);


		//cin >> A;
		//(const char *)input=A;

		cin >> c;

		int ans = solution(c, length);
        
            /*double C, F, T;
			cin >> C;
			cin >> F;
			cin >> T;
			cout.precision(10);*/

			printf("Case #%d: %d\n", i, ans);
        
    }

	getch();


	return 0;
}