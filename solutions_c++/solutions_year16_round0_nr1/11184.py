#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll n,leading;
vector<bool> found;
void init(){
	found.clear();
	for(int i=0;i<10;i++)
		found.push_back(false);
	if(n==0)
		return;
	leading = 0;
	while(n%100==0){
		n/=10;
		leading++;
	}
}

bool passes(){
	bool passes = true;
	for(int i=0;i<10;i++)
		if(!found[i])
			return false;
	return true;
}

ll foo(){
	if(n==0)
		return -1;
	ll temp = n;
	int c=2;
	while(true){
		ll aux = temp;
		while(aux!=0){
			int digit = aux%10;
			found[digit] = true;
			aux/=10;
			if(passes())
				break;
		}
		if(passes())
			break;
		temp = n*c++;
	}

	return temp*pow(10,leading);
}


int main() {
	int t=0,T;
	cin >> T;
	while(t++<T){
		scanf("%d",&n);
		init();
		ll val = foo();
		cout << "Case #" << t << ": ";
		if(val==-1)
			cout << "INSOMNIA";
		else
			cout << val;
		cout << endl;
	}
	return 0;
}