#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool P(unsigned long long x) {
  unsigned long long r = 0, n = x;

  while (n > 0)
  {
    r = r * 10 + n % 10;
    n /= 10;
  }

  return x == r;

}

void prepare(vector<long long>& vc)
{
    for(int i = 1; i <= 10000000; ++i) {
	if(P(i)) {
	    long long sq = i*i;
	    if (P(sq)) 
	    	vc.push_back(sq);
	} 
    }
}

int main() 
{
    vector<long long> vc;
    prepare(vc);

    fstream f("in", fstream::in);
    int T;
    f >> T;
    for (int i = 1; i <= T; ++i) {
	int A, B;
	f >> A >> B;
    	cout << "Case #" << i << ": ";
	long long j = 0;
	while (vc[j] < A) ++j;
	long long count = 0;
	while(vc[j++] <= B) ++count; 
	cout << count << endl;
    }
    return 0;

}
