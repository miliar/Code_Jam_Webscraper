#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-out.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large-out.txt","w",stdout);
	int T;
	cin>>T;
	for(int at=0;at<T;at++){
		printf("Case #%d: ",at+1);
		double C,F,X;
		cin >> C >> F >> X;
		double k = 2;
		int s = double(X/C - k/F);
		double ans = 0;
		for (int i=0;i<s;i++){
			ans += C/k;
			k += F;
		}
		ans += X/k;
		printf("%.9lf\n", ans);
	}
}