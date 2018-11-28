#include <iostream>
#include <cstdio>

using namespace std;

int arr[]={1,4,9,121,484};

int main() {
	int k;
	cin >> k;
	int a,b,count;
	for(int i=0;i<k;i++)
	{
		count =0;
		cin >> a>> b;
		for(int j=0;j<5;j++)
		{
			if(arr[j]<=b && a<=arr[j])
				count++;
		}
		printf("Case #%d: %d\n", i+1, count);


	}
	return 0;
}