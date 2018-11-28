#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

vector<int> set;
#define MAXIMUM 1000

int check(int n){
	char a[10];
	int i = 0;
	while(n>0){
		a[i] = n%10 + '0';
		n/=10;
		i++;
	}
	a[i] = '\0';
	int max;
	if(i%2==0) max = i/2;
	else max = (i/2)+1;
	int che = 1;
	for(int j=0;j<max;j++){
		if(a[j] != a[i-j-1])
			che = 0;
	}
	return che;
}

void create(){
	for(int i=10;i<MAXIMUM;i++){
		int temp = i*i;
		if(temp <= 1000){
			if(check(i) && check(temp))
				set.push_back(temp);
		}
	}
	//Test
	//for(int i=0;i<set.size();i++) cout << set[i] << endl;
}

void solve(int m){
	int a,b;
	int n=0;
	cin >> a >> b;
	for(int i=0;i<set.size();i++){
		if(set[i] >= a && set[i] <= b) n++;
	}
	printf("Case #%d: %d\n",m,n);
}

int main(){
	int n;
	set.push_back(1);
	set.push_back(4);
	set.push_back(9);
	create();
	cin >> n;
	for(int i=0;i<n;i++){
		solve(i+1);
	}
	return 0;
}