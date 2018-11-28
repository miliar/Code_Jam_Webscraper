#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	
	for(int j=1;j<=t;j++){
		char s[1010];
		cin>>s;
		list <int> l;
		l.push_front(s[0]);
		for(int i=1;i<strlen(s);i++){
			if(s[i]<l.front()){
				l.push_back(s[i]);
			}
			else{
				l.push_front(s[i]);
			}
		}
		printf("Case #%d: ",j);
		while(!l.empty()){
			printf("%c",l.front());
			l.pop_front();
		}
		printf("\n");
		
	}
		// your code goes here
	return 0;
}