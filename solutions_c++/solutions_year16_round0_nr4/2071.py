#include <iostream>

using namespace std;


long nextPos(long k, long c, long bit)
{
	if(c == 1)
		return bit;

	return (k*(nextPos(k, c-1, bit-1) -1) + bit);
}

void runCase(int caseNum, int k, int c, int s)
{
	if (c >= k)
		c = k;

	int num =  k/c;
	if (k%c != 0)
		num++;

	if(num > s)
	{
		cout << "Case #" << caseNum << ": IMPOSSIBLE" << endl;
		return;
	}

	cout << "Case #" << caseNum << ": ";
	long bit = c;
	for (int i=0; i<num; i++)
	{
		long loc = nextPos(k, c, bit);
		cout << loc << " ";
		bit = (bit+c <= k) ? (bit + c) : k;
	}
	cout << "\n";
}

int main()
{
  int T, K, C, S;
  int i = 0;
  cin >> T;
  for (i = 0; i < T; i++) {
    cin >> K >> C >> S;
    runCase(i+1,K,C, S);    
  }
  return 0;
}
