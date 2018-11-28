#include<iostream>
#include<algorithm>

using namespace std;

int solve(){
	int n, res = 0;
	cin >> n;
	int a[1080];
	for(int i = 0;i < n;i++)cin >> a[i];
	for(int i = 0;i < n;i++){	
		int p = 1080;
		int tmp = 0;
		for(int j = i - 1;j >= 0;j--){
			if(a[j] > a[i])tmp++;
		}
		p = min(p, tmp);
		tmp = 0;
		for(int j = i + 1;j < n;j++){
			if(a[j] > a[i])tmp++;
		}
		p = min(p, tmp);
		res += p;
	}
	return res;
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
