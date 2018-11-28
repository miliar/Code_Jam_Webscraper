#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t;
int num[10][28];
void find_ans(int a[],int now,int b[],int number){
	int i,j;
	if(number>9)return ;
	string s;
	if(number==0){
		s="ZERO";
	}
	else if(number==1){
		s="ONE";
	}
	else if(number==2){
		s="TWO";
	}
	else if(number==3){
		s="THREE";
	}
	else if(number==4){
		s="FOUR";
	}
	else if(number==5){
		s="FIVE";
	}
	else if(number==6){
		s="SIX";
	}
	else if(number==7){
		s="SEVEN";
	}
	else if(number==8){
		s="EIGHT";
	}
	else if(number==9){
		s="NINE";
	}
	int tt=1,z[30]={};
	for(i=0;i<26;i++){
		if(a[i]!=0)tt=0;
	}
	if(tt==1){
		t=1;
		for(i=0;i<now;i++){
			printf("%d",b[i]);
		}
		printf("\n");
		return;
	}
	tt=1;
	for(i=0;i<s.length();i++){
		z[s[i]-'A']++;
	}
	for(i=0;i<26;i++){
		if(a[i]<z[i]){
			tt=0;
			break;
		}
	}
	if(tt==1){
		for(i=0;i<26;i++){
			a[i]-=z[i];
		}
		b[now]=number;
		find_ans(a,now+1,b,number);
		for(i=0;i<26;i++){
			a[i]+=z[i];
		}
	}
	if(t==1)return ;
	
	find_ans(a,now,b,number+1);
}
int main(){
	int T,I;
	scanf("%d",&T);
	for(I=0;I<T;I++){
		char s[3000];
		scanf("%s",s);
		printf("Case #%d: ",I+1);
		int a[28]={},i,j,k,b[3000];
		for(i=0;i<strlen(s);i++){
			a[s[i]-'A']++;
		}
		t=0;
		find_ans(a,0,b,0);
	}
	return 0;
}