#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cctype>
#define INF 2000000000
#define M 1000000007LL

using namespace std;

int main()
{
	int T;
	cin>>T;
	int t = 0;
	while (t++<T){
		int start, end;
		cin>>start;
		int a[4];
		int tmp;
		for (int i = 1; i<=4; i++){
			for (int j = 0; j<4; j++){
				if (i==start) cin>>a[j];
				else cin>>tmp;
			}
		}
		set <int> S;
		S.clear();
		S.insert(a[0]);S.insert(a[1]);S.insert(a[2]);S.insert(a[3]);
		int cnt = 0;
		int res;
		cin>>end;
		for (int i = 1; i<=4; i++){
			for (int j = 0; j<4; j++){
				if (i==end){
					cin>>tmp;
					if (S.count(tmp)){
						cnt++;
						res = tmp;
					}
				} 
				else cin>>tmp;
			}
		}
		cout<<"Case #"<<t<<": ";
		if (cnt==0) cout<<"Volunteer cheated!"<<endl;
		if (cnt==1) cout<<res<<endl;
		if (cnt>1) cout<<"Bad magician!"<<endl;
	}
}