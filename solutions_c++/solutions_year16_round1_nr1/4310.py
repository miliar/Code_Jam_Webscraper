#include <bits/stdc++.h>

using namespace std;

void printList( list<char>* l ){
	for(list<char>::iterator i = l->begin(); i != l->end(); ++i)
		printf("%c", *i);
	printf("\n");
}

list<char> solve(){
	string s;
	cin >> s;
	int ssize = s.size();
	list<char> lw (ssize-1);
	lw.push_front(s[0]);
	for(int i = 0; i < ssize -1  ; i++){
		//cout << "front: " << lw.front() << " ";
		//cout << "s[i+1] " << s[i+1] << endl;
		if( lw.front() <= s[i+1] )
			lw.push_front(s[i+1]);
		else
			lw.push_back(s[i+1]);
		//printList(&lw);
	}
	return lw;
}
int main(){
	int T;
	scanf("%d\n", &T);
	for( int t = 0; t < T; t++){
		list<char> s = solve();
		printf("Case #%d: ", t+1);
		printList(&s);
	}

}