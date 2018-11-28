#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
	//freopen("1.txt","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-out.txt","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large-out.txt","w",stdout);
	int T;
	cin>>T;
	for(int at=0;at<T;at++){
		printf("Case #%d: ",at+1);
		int n, m;
		cin >> n;
		vector<int> a(16);
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++){
				int c;
				cin >> c;
				if (i == n)
					a[c-1] = 1;
			}
		cin >> m;
		vector<int> ans;
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++){
				int c;
				cin >> c;
				if (i == m && a[c-1] == 1)
					ans.push_back(c);
			}
		if (ans.size() == 0)
			printf("Volunteer cheated!\n");
		else
			if (ans.size() > 1)
				printf("Bad magician!\n");
			else
				printf("%d\n", ans[0]);
	}



}