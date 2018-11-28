#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>

using namespace std;
int rna(int m);
int main(){
	int t;
	scanf("%d",&t);
	int c=1;
	while(c<=t){
		int m;
		scanf("%d",&m);
		int required_people;
		required_people=rna(m);
		printf("Case #%d: %d\n",c,required_people);
		c++;
	}
	return 1;
}

int rna(int m){
	string s;
	cin>>s;
	int np=s[0]-'0';
	int nr;
	int t=0;
	int na=0;
	for(int i=1;i<=m;i++){
		nr=i;
		if(s[i]-'0'==0){
			continue;
		}
		if(nr>np){
			
			na+=(nr-np);
			np+=nr-np;
			// t=nr-np;
			
		}
		np+=s[i]-'0';
	}
	return na;
}
