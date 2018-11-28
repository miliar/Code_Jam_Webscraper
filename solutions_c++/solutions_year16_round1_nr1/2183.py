
#include<stdio.h>
#include<string>
#include<iostream>
#define B int testb;scanf("%d", &testb);int t = testb;while(t--)
using namespace std;
int main(){
	string c,a;
	char p;
	int i;
	B{
		cin>>c;
		printf("Case #%d: ", testb-t);
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
