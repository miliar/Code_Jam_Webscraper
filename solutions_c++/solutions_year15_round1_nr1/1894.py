#include <iostream>
#include <set>
#include <vector>
#include <string>
using namespace std ;
void main(){
	int T ;
	cin >> T ;
	for(int t=0;t<T;t++) {
		int N, v, o ;
		cin >> N ;
		int r=0, y = 0 ;
		vector<int> arr ;
		for(int n=0;n<N;n++) {
			cin >> v ;
			arr.push_back(v);
			if(n>0 && o>v) y+= o-v ;
			if(n>0 && o-v>r) r= o-v;
			o = v ;
		}
		int x = 0;
		for(int n=0;n<N-1;n++) {
			if(arr[n]>r) x+=r ;
			else x+=arr[n] ;
		}
		cout << "Case #" << t+1 << ": " << y << ' ' << x << endl;
	}
}