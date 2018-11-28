#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
typedef pair<bool, int> PBI;
int ans = -1;
void print ( int kase ,  string yes )
{
 	 cout <<"Case #"<<kase<<": ";
	 cout<<yes;
	 cout <<"\n";
 	 return ;
}

int main(){
	int T, kase = 0; cin >> T;
	while (T--) {
		int N; cin >> N; N--;
		int arr[5], tmp;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) if (i == N) cin >> arr[j];
		else cin >> tmp;
		cin >> N;N--;
		int cnt = 0;
		for (int i = 0 ;i < 4; i++) for (int j = 0;j < 4; j++) {
			cin >> tmp;
			if (N == i)for (int k = 0; k < 4; k++) if (tmp == arr[k]) ans = tmp, cnt++;
		} 
		if (cnt == 0) print(++kase, "Volunteer cheated!");
		else if (cnt ==1) cout <<"Case #"<<++kase<<": " << ans<<"\n";
		else print(++kase, "Bad magician!");
	}
}
