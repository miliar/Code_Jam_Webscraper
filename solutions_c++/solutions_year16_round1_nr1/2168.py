//The Last Word
#include<stdio.h>
#include<string>
#include<iostream>
#define T int test;scanf("%d", &test);int t = test;while(t--)
/*void nextString(char* c){
	int i=0;
	char d = getchar_unlocked();
	while(d != ' ' && d != '\n'){
		c[i++] = d;
		d = getchar_unlocked();
	}
	c[i] = '\0';
}*/
using namespace std;
int main(){
	string c,a;
	char p;
	int i;
	T{
		cin>>c;
		printf("Case #%d: ", test-t);
		p = c[1];
		i = 1;
		a = c[0];
		while(p != '\0'){
			if(p>=a[0]){
				a = p + a;
			}
			else{
				a = a + p;
			}
			p = c[++i];
		}
		printf("%s\n",a.c_str());
	}
}
