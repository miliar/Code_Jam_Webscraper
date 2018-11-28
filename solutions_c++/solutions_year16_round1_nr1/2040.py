
#include<iostream>
#include<stdio.h>
#include<list>
#include<string.h>
using namespace std;

int main(){
    freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);
    int T;
	scanf("%d",&T);
	getchar();
	int j=1;
	while(j<=T){

        char s[1000];
        gets(s);
        list<char> output;
        output.push_back(s[0]);
        for(int i=1;i<strlen(s)&& s[i]!='/0';i++){
            if(s[i]>=*output.begin())
                output.push_front(s[i]);
            else output.push_back(s[i]);
        }
        list<char>::iterator a=output.begin();
        printf("Case #%d: ",j);
        while(a!=output.end()){
            printf("%c",*a);
            a++;
        }
        printf("\n");
        output.clear();
        j++;
	}
}
