#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;
const int MAX = 1000 + 10;

int bit[MAX];
int rec[MAX];

struct emt{
	int id, val;
	emt(int _id = 0, int _val = 0):id(_id),val(_val){}
	bool operator<(const emt &a)const{
		return val < a.val;
	}
}arr[MAX];

int main(){
	freopen("Blarge.in", "r", stdin);
	freopen("Blarge.out", "w", stdout);
	int TN;
	scanf("%d", &TN);
	for(int casen = 1 ; casen <= TN ; casen++){
		int n;
		scanf("%d", &n);
		for(int i = 0 ; i < n ; i++){
			arr[i].id = i;
			scanf("%d", &arr[i].val);
		}
		sort(arr, arr+n);
		int cnt = 1;
		for(int i = 0 ; i < n ; i++){
			rec[arr[i].id] = cnt;
			cnt++;
		}
		int ans = 0;
		for(int i = 0 ; i < n ; i++){
			int tmp = arr[i].id;
			if(tmp < (n-i)/2){
				ans += tmp;
			}else{
				ans += n-i-tmp-1;
			}
			for(int j = i+1 ; j < n ; j++)
				if(arr[j].id > tmp) arr[j].id--;
		}
		printf("Case #%d: %d\n", casen, ans);
	}
	return 0;
}
