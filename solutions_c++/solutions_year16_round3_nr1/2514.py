#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int j = 0; j<t; j++){
		int n;
		cin>>n;
		int a[n], sum = 0;
		for(int i = 0; i<n; i++){
			cin>>a[i];
			sum += a[i];
		}
		//int s = sum;
		//cout<<sum<<" ";
		int ch[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
		cout<<"Case #"<<j+1<<": ";
		int c = 0;
		if(sum%2==0){
		while(sum>0){
			int lar = -1;
			int k;
			for(int i = 0; i<n; i++){
				if(a[i]>lar){
					lar = a[i];
					k = i;
				}
			}
			if(c<2){
				cout<<char(ch[k]);
				a[k]--;
				sum--;
				c++;
			}
			else{
				c = 0;
				cout<<" ";
			}
		}}
		else{
			c = 0;
			int d = (sum-3);
			while(d>0){
				int lar = -1;
				int k;
				for(int i = 0; i<n; i++){
					if(a[i]>lar){
						lar = a[i];
						k = i;
					}
				}
				if(c<2){
					cout<<char(ch[k]);
					a[k]--;
					sum--;
					c++;
					d--;
				}
				else{

					c = 0;
					cout<<" ";
				}
			}
			for(int i = 0; i<n; i++){
				if(a[i]>0){
					cout<<" "<<char(ch[i])<<" ";
					a[i]--;
					break;
				}
			}
			for(int i = 0; i<n; i++){
						if(a[i]>0){
							cout<<char(ch[i]);
						a[i]--;
						break;
					}

					}
			for(int i = 0; i<n; i++){
				if(a[i]>0){
					cout<<char(ch[i]);
					a[i]--;
					break;
				}

			}
			sum = 0;
		}

		cout<<endl;
	}
	return 0;
}
