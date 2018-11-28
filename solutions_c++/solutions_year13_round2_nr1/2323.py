#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int getNum(int A, int d, int& sum)
{
	int k = 1;
	int val = (A-1)*2;
	sum = 1+val;
	while(sum < d){
		k++;
		val*=2;
		sum = 1+val;
	}
	return k;
}

int getMinOps(int A, int i, const vector<int> &inData)
{
	if (i >= inData.size())
		return 0;
	if (A == 1)
	{
		return inData.size() - i;
	}
	if (inData[i] < A) {
		return getMinOps(A+inData[i], i+1, inData);
	} else {
		/*
		int minops = 1 + getMinOps(A, i+1, inData);
		int diff = inData[i] - A;
		if (diff < A-1) {
			minops = min(minops, 1 + getMinOps(2*A-1, i+1, inData));
		} else {
			int sum;
			int num = getNum(A, inData[i], sum);
			minops = min(minops, num + getMinOps(sum+inData[i], i+1, inData));
		}
		return minops;
		*/
		return min(1+getMinOps(A, i+1, inData), 1+getMinOps(2*A-1, i, inData));
	}
}
int main(int argc, char* argv[])
{
	int T;
	cin >> T;

	for (int caseId = 1; caseId <= T; caseId++)
	{
		int A, N;
		cin >> A >> N;

		vector<int> inData(N, 0);
		for (int i = 0; i < N; i++)
			cin >> inData[i];

		sort(inData.begin(), inData.end());

		int ops = getMinOps(A, 0, inData);	
		cout << "Case #" << caseId << ": " << ops << endl;
	}


	return 0;
}

