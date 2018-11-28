#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

	
int main()
{
	int a[5] = {1, 4, 9, 121, 484 };
	int t;
	cin >> t;
	int t2 = 1;
	int a1, b1;
	while(t--) {
		cin >> a1 >> b1;
		int count = 0;
		for(int i = 0; i < 5; i++) {
			if(a[i] >= a1 && a[i] <= b1) { 
			count++;
			}
		}
		
		cout << "Case #" << t2 << ": " <<  count << endl;
		t2++;
	}
	return 0;
}
		