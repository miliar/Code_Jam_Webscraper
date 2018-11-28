/*
bool decending(int x, int y)
{
	return x>y;
}

void permute(vector<int>::iterator it, vector<int>::iterator it2)
{
	
}

long long int minScalarProd(vector<int>::iterator it, vector<int>::iterator it2, int size)
{
	int ans = 0;
	for(int x = 0; x < size; x++)
		ans += (*(it+x))*(*(it2+x));
//		ans += it[x]*it2[x];
//		ans += *(it++)*(*(it2++)); 
	return ans; 
}
	int numTest = 0, testCase = 1;
//	int a = 0b00000010, b = 0b00000001, c = a&b;	// for some reason cant cout << a&b;?
	long long int m1A = 0, m2B = 0, K = 0, wingPairs = 0;

	cin >> numTest;

	while(numTest > 0)
	{
		cin >> m1A >> m2B >> K;	

		for(long long int z = 0b000000; z < K; z++)
			for(long long int x = z; x < m1A; x++)
				for(long long int y = z; y < m2B; y++)
				{
					if((x&y)==z)
					{
						wingPairs++;
		//				cout << endl << x << y << z;
					}
				}
				
				

		if(testCase != 1)
			cout << endl;
	//	permute(v1.begin(), v2.begin());	// Order elements to result in minimum prod
	//	sort(v1.begin(), v1.end());
	//	sort(v2.begin(), v2.end(), decending);

		cout << "Case #" << testCase << ": " << wingPairs;
		numTest--;	
		testCase++;

		wingPairs = 0;
	}


*/

// Only completes the small input
#include <iostream>
#include <vector>
//#include <algorithm>

using namespace std;

		//0,1,2,3,4,5,6,7,8,9
int digits[10] = {0,0,0,0,0,0,0,0,0,0};

bool done(void)
{
	int sum = 0;
	for(int i = 0; i < 10; i++)
		sum += digits[i];
	if(sum == 10)
		return true;
	else
		return false;
}	

bool check(long long int N)
{
	while(N)
	{
		for(int i = 0; i < 10; i++)
			if(!digits[i])
				if(i == N%10)
				{
					digits[i] = 1;
					if(done())
						return true;
				}
		N /= 10;
	}
	return false;
}

int main(void)
{
	int numTest, lNum, caseNum = 1;
	long long int N;

	// Get num test cases;
	cin >> numTest;
	while(numTest)
	{
		cin >> N;

		for(int s = 0; s < 10; s++)			// reset
			digits[s] = 0;

		if(N == 0)
		{
			cout << "Case #" << caseNum << ": " << "INSOMNIA" << endl;
			numTest--;
			caseNum++;
			continue;
		}

		for(long long int i = 1;; i++)
			if(check(i*N))
			{
				lNum = i*N;
				break;
			}

		cout << "Case #" << caseNum << ": " << lNum << endl;
		numTest--;
		caseNum++;
	}

	return 0;
}
