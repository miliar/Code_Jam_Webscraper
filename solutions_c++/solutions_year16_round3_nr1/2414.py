#include<iostream>
#include<queue>
#include<stdio.h>

using namespace std;

struct S {
 char c;
 int x;
S(char p, int q){
	c = p;
	x = q;
}
};
bool operator < ( S a, S b ) {
	return a.x < b.x;
}
int main(){

	int t, o = 0;
	cin >> t;
	while ( t-- ) {
		o++;
		int n;
		cout << "Case #" << o<<":";
		cin >> n;
		int ans = 0;
		priority_queue<S> q;
		for ( int i =0 ; i < n; i++ ) {
			int x;
			cin >> x;
		 	q.push(S('A'+i,x));
			ans += x;
		}
		while ( !q.empty() ) {
			S top = q.top();
			q.pop();
			cout << " " << top.c;
			top.x--;
			ans--;
			if ( top.x > 0 )
			q.push(top);
			if ( !q.empty() ) {
			S top = q.top();
			q.pop();
			if ( top.x > ans - top.x  ){
			cout << top.c;
			ans--;
			top.x--;
			}
			if ( top.x > 0 )
			q.push(top);
		}
		}
		cout << endl;
	}
	return 0;
}
