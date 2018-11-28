#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
string s;
int len;
int findd(int x){
	int i;
	for(i=x;i<len;i++){
		if(s[i]!='-'){
			break;
		}
	}
	return i;
}
int main(){
	int t;
	scanf("%d",&t);
	int time=0;
	while(t--){
		cin>>s;
		time++;
		len=s.size();
		int res=0;
		int i=0;
		if(s[0]=='-') {
			i=findd(0);
			res+=1;
		}
		while(i<len){
			if(s[i]=='-')
			{
				i=findd(i);
				res+=2;
			}
			i++;
		}
		printf("Case #%d: %d\n",time,res);
	}
	return 0;
}
