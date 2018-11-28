#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

int T;
int counter;
vector<int> A;


int main()
{
	int i, j;
	int begin, end, temp;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("palinn.txt","w",stdout);

	scanf("%d", &T);

	A.push_back(1);
	A.push_back(4);
	A.push_back(9);
	A.push_back(121);
	A.push_back(484);
	A.push_back(10201);
	A.push_back(12321);
	A.push_back(14641);
	A.push_back(40804);
	A.push_back(44944);
	A.push_back(1002001);
	A.push_back(1234321);
	A.push_back(4008004);
	A.push_back(10002001);
	A.push_back(102030201);
	A.push_back(104060401);
	A.push_back(121242121);
	A.push_back(123454321);
	A.push_back(125686521);


	for(i=0; i<T; i++)
	{
		scanf("%d %d", &begin, &end);
		for(j=0; j<A.size(); j++)
			if(A[j]>=begin && A[j]<=end)
				counter++;
		printf("Case #%d: %d\n", i+1, counter);
		counter=0;
	}


	return 0;
}