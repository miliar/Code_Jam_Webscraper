#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;
int T,A,N;
int arr[101];
priority_queue<pair<int,pair<int,int>>> pq;
pair<int, pair<int,int>> element,element2;

int main(int argc, char *argv[])
{
	int t;
	int i,j;
	int times,mote,index;

	scanf("%d\n", &T);
	for (t=0;t<T;t++)
	{
		printf("Case #%d: ", t+1);
		scanf("%d %d\n", &A, &N);
		for (i=0; i<N; i++)
			scanf("%d", arr+i);
		sort(arr, arr+N);
		while(!pq.empty()) pq.pop();
		element.first = 0;
		element.second.first = A;
		element.second.second = 0;
		pq.push(element);
		while(!pq.empty())
		{
			element = pq.top();
			pq.pop();
			if (element.second.second==N)
				break;
			times = element.first;
			mote = element.second.first;
			index = element.second.second;
			if (mote>arr[index])
			{
				element2 = element;
				element2.second.first += arr[index];
				element2.second.second++;
				pq.push(element2);
			}
			else
			{
				// delete
				element2 = element;
				element2.first--;
				element2.second.second++;
				pq.push(element2);
				// 2*x-1
				element2 = element;
				element2.first--;
				element2.second.first = 2*mote-1;
				pq.push(element2);
			}
		}
		printf("%d\n", -element.first);
	}
	return 0;
}