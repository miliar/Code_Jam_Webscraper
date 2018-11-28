#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
void main(){
	
	freopen("sheep.in", "r", stdin);
    freopen("sheep.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
	int n;
	for (int t = 1; t <= T; t++){
		int sheep[10]={0,0,0,0,0,0,0,0,0,0};
		int d = 10;
		int n1,k;
		cin >> n;
		n1=n;k=1;
		cout << "Case #" << t << ": ";
		if (n ==0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		else{
			//n1=n;
			//k=1;
			while (d >0){
				while (n1 >0){
					if(sheep[n1%10]==0){
						d--;
						sheep[n1%10]=1;
						
					}
					n1 /=10;
				}
				k++;
				n1 = n*k; 
			}
		}
		n1-=n;
		cout << n1 << endl;
	}
}