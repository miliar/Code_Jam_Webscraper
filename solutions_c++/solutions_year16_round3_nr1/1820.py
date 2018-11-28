#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int arr[30],n;

int get() {
	int findex = 0,value=-1; 
	for(int i = 0 ; i < n ; i ++) {
		if(arr[i] > value) {
			value = arr[i];
			findex = i;
		}
	}
	return findex;
}
int main()
{
	int t,cas=1;
	cin >> t;
	while(t--) {
		memset(arr,0,sizeof(arr));
		int tot = 0;
		cin >> n;
		for(int i = 0; i < n ; i++) {
			cin >> arr[i];
			tot += arr[i];
		}
		printf("Case #%d:",cas++);
		if(tot % 2 == 1) {
			int findex = get();
			arr[findex] -= 1;
			tot -= 1;
			printf(" %c",char('A'+findex));
		}
		while(tot > 0) {
			int findex = get();
			arr[findex] -= 1;
			tot -= 1;
			printf(" %c",char('A'+findex));
			if(tot==0)
				break;
			findex = get();
			arr[findex] -= 1;
			tot -= 1;
			printf("%c",char('A'+findex));
		}
		printf("\n");
	}
	return 0;
}

