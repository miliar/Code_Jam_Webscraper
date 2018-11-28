#include<iostream>
using namespace std;

int main(){
	int n, extra, maxs, count, N;
	char s;
	cin >> n;
	N=n;
	while(n--){
		extra = 0;
		count = 0;
		cin >> maxs;
		for(int i=0; i<=maxs; i++){
			cin >> s;
			if(i>count){
				extra += (i-count);
				count += (i-count);
			}
			count += (s-'0');
		}
		cout << "Case #" << (N-n) <<  ": " << extra << endl;		
	}
	return 0;
}
