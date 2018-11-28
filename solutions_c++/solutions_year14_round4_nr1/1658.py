#include<iostream>

using namespace std;

int num[710];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int ntc,n,c,x,res;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		res = 0;
		cout << "Case #" << tc << ": ";
		cin >> n >> c;
		memset(num,0,sizeof(num));
		for (int i=0;i<n;i++){
			cin >> x;
			num[x]++;
		}
		int k=1,p;
		while(k!=c+1){
			while(num[k]){
				num[k]--;
				p = c-k;
				for (;p>=k;p--){
					if (num[p]){
						num[p]--;
						break;
					}
				}
				res++;
			}
			k++;
		}
		cout << res<< endl;
	}

	return 0;
}