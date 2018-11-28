#include <iostream>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int findMin(int n, int x){
	if(n == x) return x;
	if(n <= 2*x)
		return x+1;

	return 1+findMin(max(2*x-1,n-x) , x);
}

int main(){
	ios::sync_with_stdio(false);
	freopen("gcj1.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,c=1, rows, cols, x;
	cin>>t;
	while(t--){
		cout<<"Case #"<<c++<<": ";
		cin>>rows>>cols>>x;
		cout<<findMin(cols,x)<<endl;
	}


	return 0;
}