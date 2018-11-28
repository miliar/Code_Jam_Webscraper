#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue> 

using namespace std;

#define MP make_pair
#define PB push_back
#define MOD 1000000007
#define INF 1000000000

int main(){
	int t,tt,ind;
	cin >> t;
	tt=t;
	while(t--) {
		long long int n,temp,curr;
		int arr[10] = {0};
		int i,count=0,flag=0;
		cin >> n;
		printf("Case #%d: ",tt-t);
		if (n == 0) {
			cout << "INSOMNIA" <<endl;
		} else {
			for(i=1;i<10000;i++){
				curr=n*i;
				temp=curr;
				while(curr>0){
					ind=curr%10;
					if(arr[ind]==0){
						arr[ind]=1;
						count++;
					}
					curr /= 10;
				}
				if (count >= 10){
					cout << temp << endl;
					flag = 1;
					break;
				}
			}
			if (flag == 0) {
				cout << "INSOMNIA" <<endl;
			}
		}
	}
	return 0;
}
