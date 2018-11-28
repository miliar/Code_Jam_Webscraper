#include<string>
#include<iostream>

using namespace std;

#define		MAX		1010

int num[MAX];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int ntc,n,res,mn;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		for (int i=0;i<n;i++) cin >> num[i];
		cout << "Case #" << tc << ": ";
		res = 0;mn = 0;
		for (int i=1;i<n;i++){
			if (num[i-1]>num[i]){
				res+= num[i-1]-num[i];
				mn = max(mn,num[i-1]-num[i]);
			}
		}
		cout << res << " ";
		res = 0;
		for (int i=0;i<n-1;i++){
			res+= min(num[i],mn);
		}
		cout << res << endl;

	}

	return 0;
}