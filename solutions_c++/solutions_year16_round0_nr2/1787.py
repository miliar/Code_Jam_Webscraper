#include <algorithm>
#include <stdio.h>
#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int find_last_m(string s){
	int N = s.length();
	for(int i=N-1; i>=0; i--){
		if(s[i]=='-') return i;
	}
	return -1;
}

int find_first_m(string s){
	int N = s.length();
	for(int i=0; i<N; i++){
		if(s[i]=='-') return i;
	}
	return -1;
}


void change_side(char& c){
	if(c=='-') c='+';
	else c='-';
}

void reverse(string& s, int n){
	int i=0;
	int j=n;
	while(j>=i){
		if(i==j){
			change_side(s[i]);
			break;
		}
		swap(s[i],s[j]);
		change_side(s[i]);
		change_side(s[j]);
		i++;
		j--;
	}
}

int main(){
	int T, cur, N;
	string s;
	ifstream input("B-large.in");
	//freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	//scanf("%d",&T);
	input>>T;
	//cout<<T;
	getline(input,s);
	for(int i=0; i<T; i++){
		printf("Case #%d: ",i+1);
		//scanf("%s",&s);
		getline(input,s);
		//cout<<s;
		N = 0;
		while(true){
			cur = find_last_m(s);
			//cout<<cur<<endl;
			if(cur==-1) break;
			if(s[0]=='-'){
				reverse(s,cur);
				N++;
			}
			else{
				int fir = find_first_m(s);
				reverse(s,fir-1);
				reverse(s,cur);
				N+=2;
			}
		}
		cout<<N<<endl;
	}
	return 0;
}