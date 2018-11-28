#include <iostream>
#include <vector>
#include <cmath>
#include <math.h>
#include <algorithm>
using namespace std;


void DoSolve(int test, int N, vector<int>& mushrooms)
{
	int m1 = 0;
	int m2 = 0;
	int rate = 0;
	for (size_t i=0; i< (mushrooms.size() - 1); ++i) {
		int delta = mushrooms[i+1]-mushrooms[i];
		m1 += ((delta <= 0) ? (abs(delta)):0);

		if (delta < 0 && (abs(delta) > rate)) {
				rate = abs(delta);
		}
	} //for

	for (size_t i=0; i<(mushrooms.size() - 1); ++i) {
		m2 += min(rate,mushrooms[i]);
	}

	cout<<"Case #"<<test<<": "<<m1<<" "<<m2<<endl;

}


int main()
{
	int T;
	int N;

	cin>>T;
	
	for (int test=1; test<=T; ++test) {
		cin>>N;
	  vector<int> mushrooms;
		for (int mush=1; mush<=N; ++mush) {
			int temp;
			cin>>temp;
			mushrooms.push_back(temp);
		}
		DoSolve(test,N,mushrooms);
	}

	return 0;
}
