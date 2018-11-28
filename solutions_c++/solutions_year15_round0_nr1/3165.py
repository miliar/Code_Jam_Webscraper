#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.txt","w",stdout);
	int T;
	cin>>T;
	for(int at=0;at<T;at++){
		printf("Case #%d: ",at+1);
		int n;
		string s;
		cin >> n >> s;
		int add = 0;
		int cnt = 0;
		for(int i=0;i<s.size();i++){
			int d = s[i] - '0';
			if (i > cnt){
				add += i - cnt;
				cnt = i;
			}
			cnt += d;
		}
		printf("%d\n", add);		

	}



}