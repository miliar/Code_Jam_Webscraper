#include <iostream>
#include <vector>

using namespace std;

int getNum(vector<int> v){
	for(int i = 0; i < 10; i++){
		if(v[i] == 0) return 0;
	}
	return 10;
}

int make(int x, vector<int> &v){
	do{
		v[x % 10]++;
		x /= 10;
	}while(x);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n, i;
	cin>>t;
	for(i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		cin>>n;
		vector<int> v(10);
		if(n == 0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		else{
			int x = n;
			make(x, v);
			while(getNum(v) < 10){
				x += n;
				make(x, v);
			}
			cout<<x<<endl;
		}
	}
}
