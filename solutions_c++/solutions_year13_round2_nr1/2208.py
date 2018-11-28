#include <cstdio>
#include <iostream>
#include <cstring>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;
#define MAXN 1000000
int a[MAXN];
int curmax = 0;

int cal(int size, int a[], int n, int cnt){
	int end = n;
	bool flag = true;
	int maxv = 0;
	int maxi = 0;
	while(end != 0){
		flag = false;
		for(int i = 0; i < end; i++){
			if(maxv < a[i])
			{
				maxv = a[i];
				maxi = i;
			}
			if(size > a[i]){
				size += a[i];
				end--;
				std::swap(a[i], a[end]);
				i--;
				flag = true;
			}
		}
		if(flag == false){
			break;
		}
	}
	if(flag)
		return cnt;
	else if(size <= 1){
		return cnt + end;
	}
	else{
		int left = cal(size+size-1, a, end, cnt+1);
		swap(a[maxi], a[end-1]);
		int right = cal(size, a, end-1, cnt+1);
		swap(a[maxi], a[end-1]);
		return min(left, right);
	}
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++){
        cout << "Case #" << cases << ": ";
		int size;
		int n;
		cin >> size >>  n;
		for(int i = 0; i < n; i++){
			cin >> a[i];
		}
		int end = n;
		curmax = n;
		int res = cal(size, a, end, 0);



        cout << res <<  endl;
	}
	//system("pause");
	return 0;
}
