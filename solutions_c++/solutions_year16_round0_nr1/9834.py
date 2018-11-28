/*

 *
 */

#define XWON	0
#define OWON	1
#define DRAW	2
#define NCMP	3
 
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>



using namespace std;

int solve(int N)
{
	int mask = 0xFFFFFC00;			// 10 bits as zeros
	int inv_mask = 0xFFFFFFFF;
	
	int i;
	for(int i = 1; i < 100; i++) {
		
		int num = i * N;
		
		if(num == 0)		mask = mask | 1;
		else {
			int d;
			for(int j = 10; num != 0;) {
					d = num % j;
					mask = mask | (1 << d);
					num = num / j;
					
					if(mask == inv_mask)
						return i * N;
			}			
		}
		
		
	}
	
	return 0;		
}


int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("A-small-attempt0.in", ios::in);
	outf.open("output.txt");


	int T;
	int result;
	string line;
	
	inf >> T;
	// get one test case
	for(int i = 0; i < T; i++)
	{		
		int N;
		inf >> N;
				
		int result = solve(N);
		if(result == 0)	{
			cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
			outf << "Case #" << (i+1) << ": INSOMNIA" << endl;
		}
		else 				{
			cout << "Case #" << (i+1) << ": " << result << endl;
			outf << "Case #" << (i+1) << ": " << result << endl;
		}
		//outf << "Case #" << (k+1) << ": ";		
	}


	inf.close();
	outf.close();
	return 0;
}
