#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;


int main(){
	//freopen("1.txt","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-out1.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large-out.txt","w",stdout);
	int T;
	cin>>T;
	for(int at=0;at<T;at++){
		printf("Case #%d: ",at+1);
		int n;
		cin >> n;
		vector<int> a(n);
		for(int i=0;i<n;i++)
			cin >> a[i];
		int ans = -1;
		for(int k=1;k<=1000;k++){
			int cnt = 0;
			for(int i=0;i<n;i++)
				cnt += (a[i] + k - 1) / k - 1;
			if(ans == -1) ans = cnt + k;
			if(ans > cnt + k) ans = cnt + k;
		}
		printf("%d\n", ans);
	}
}