#include <bits/stdc++.h>
#define MAX 10e9+7

using namespace std;
typedef unsigned long long ull;

void sorta(int* a, int* pos, int n){
	int temp;
	for(int i=0; i<n; i++){
		for(int j=0; j<n-i-1; j++){
			if(*(a+j) < *(a+j+1)){
				temp = *(a+j);
				*(a+j) = *(a+j+1);
				*(a+j+1) = temp;
				temp = *(pos+j);
				*(pos+j) = *(pos+j+1);
				*(pos+j+1) = temp;
			}
		}
	}
}

int sum(int a[], int n){
	int count = 0;
	for(int i=0; i<n; i++){
		count += a[i];
	}
	return count;
}

void print(int a[], int pos[], int n){
	float per;
	int count;
	int flag = 0;
	a[0] -= 2;
	count = sum(a,n);
	for(int i=0; i<n; i++){
		per = float(a[i])/count;
		if(per>0.5){
			a[0] += 2;
			flag = 1;
			break;
		}
	}
	if(!flag){
		cout << (char)(65+pos[0]) << (char)(65+pos[0]) << " ";
		return;
	}
	flag = 0;
	a[0]--;
	a[1]--;
	count = sum(a,n);
	for(int i=0; i<n; i++){
		per = float(a[i])/count;
		if(per>0.5){
			a[0]++;
			a[1]++;
			flag = 1;
			break;
		}
	}
	if(!flag){
		cout << (char)(65+pos[0]) << (char)(65+pos[1]) << " ";
		return;
	}
	flag = 0;
	a[0]--;
	count = sum(a,n);
	for(int i=0; i<n; i++){
		per = float(a[i])/count;
		if(per>0.5){
			a[0]++;
			flag = 1;
			break;
		}
	}
	if(!flag){
		cout << (char)(65+pos[0]) << " ";
	}
}

void plan(int a[], int n){
	int count = sum(a,n);
	int counter = 0;
	int pos[n];
	char c = 65;
	for(int i=0; i<n; i++){
		pos[i] = i;
	}
	do{
		sorta(a,pos,n);
		// for(int i=0; i<n; i++){
		// 	cout << a[i] << pos[i] << endl;
		// }
		counter = 0;
		print(a,pos,n);
		//cout << " ";
		count = sum(a,n);
	}while(count > 0);
}

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.io","w",stdout);
	int test,n,p,i=1;
	int a[27];
	cin >> test;
	while(i<=test){
		cin >> n;
		for(int j=0; j<n; j++){
			cin >> a[j];
		}
		cout << "Case #" << i << ":" << " ";
		plan(a,n);
		cout << endl;
		i++;
	}
	return 0;
}