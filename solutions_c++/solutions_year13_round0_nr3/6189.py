#include "stdio.h"
#include "assert.h"
#include "time.h"
#include "stdlib.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	std::ifstream in("C-small-attempt1.in");
    std::streambuf *cinbuf = std::cin.rdbuf();
    std::cin.rdbuf(in.rdbuf());

	std::ofstream out("C-small-attempt1.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	

	vector <int> arr(1001,0);

	int tmp = 1;
	for(int i = 1; i < 1002; i++)
	{
		if (i == 1 || i == 4 || i == 9 || i == 121 || i == 484)
			
		arr[i-1] = 1;
	}

	int testNum = 0;
	cin >> testNum;

	for (int i = 0; i < testNum; i++){
		int A,B;

		cin >> A >> B;

		int sum = 0;
		for (int j = A-1; j <= B-1; j++)
		{
			sum += arr[j];
		}

		cout << "Case #" << i+1 << ": " << sum << endl;
	}

	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);

    float time = ((float)clock()) / CLOCKS_PER_SEC;
    printf("profiling time: %f\n", time);

	system("pause");

	return 0;
}