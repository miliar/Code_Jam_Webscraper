#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
#define MAX(x,y) (x > y ? x : y)
#define MIN(x,y) (x > y ? y : x)
 
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int idx = 1; idx <= T; idx++) {
		int ans = 0, mask = 0;
		int a, b;
		cin>>a;
		for(int i =1; i<=4; i++)
			for(int j = 0; j < 4;j++) {
				int x;
				cin>>x;
				if ( a == i) {
					mask += (1<<x);
				}
			}
		cin>>b;
		for(int i =1; i<=4; i++)
			for(int j = 0; j < 4;j++) {
				int x;
				cin>>x;
				if ( b == i) {
					if ((mask & (1<<x)) != 0) {
						if (ans == 0)
							ans = x;
						else if (ans > 0)
							ans = -1;
					}
				}
			}
		cout << "Case #"<< idx<< ": ";
		switch (ans) {
		case -1:
			cout<<"Bad magician!";
			break;
		case 0:
			cout<<"Volunteer cheated!";
			break;
		default:
			cout<<ans;
			break;
		}
		cout << endl;
	}
	return 0;
}