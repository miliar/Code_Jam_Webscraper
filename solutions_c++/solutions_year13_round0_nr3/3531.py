#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<queue>
#include<cmath>



#define MAX 1001
#define N 100001
#define LL 3

using namespace std;


struct cr{
	char a[LL];
};
typedef struct cr cr;

int pos,num[N];


void chk1(char tmp[110]){

	int l;

	l=strlen(tmp);
	
	int i,tt=0,s,ss,t=0;

	

	for(i=0;i<l;i++){
		tt=tt*10+(tmp[i]-'0');
	}

	s=sqrt(tt);

	if(s*s==tt){
	
		ss=s;
		while(ss){
			t=t*10+(s%10);
			ss=ss/10;
		}
		if(s==t){
			num[pos++]=tt;
		}

	}

}

void isSqrPalindram(char tmp[110]){

	chk1(tmp);
	

	

}


void calcPalindram(){


	queue<cr> q;

	cr crt,tp;

	int i;



	char tmp[110],ttt[2];

	for(i=1;i<=9;i++){
		ttt[0]='0'+i;
		ttt[1]=NULL;
		strcpy(tp.a,ttt);
		if(strlen(tp.a)<LL){
			q.push(tp);
		}	
		isSqrPalindram(tp.a);
	}

	while(q.size()){
		crt=q.front();
		q.pop();

		strcpy(tmp,crt.a);
		strcat(tmp,strrev(crt.a));
		isSqrPalindram(tmp);

		for(i=0;i<=9;i++){
			strcpy(tmp,crt.a);
			ttt[0]='0'+i;
		ttt[1]=NULL;
			strcat(tmp,ttt);
			
			strcpy(tp.a,tmp);
			if(strlen(tp.a)<LL){
				q.push(tp);
			}
			
			
			strcat(tmp,strrev(crt.a));
			isSqrPalindram(tmp);	
		}
		
	}




}

int getAmount(){

	int x,y,i=0,j=0;

	scanf("%d%d",&x,&y);

	while(i<pos && num[i]<x){
		i++;
	}

	while(j<pos && num[j]<=y){
		j++;
	}

	return j-i;	

}

int main(){

	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);

	calcPalindram();

	int cases,i;

	//printf("pos %d",pos);

	scanf("%d",&cases);

	for(i=1;i<=cases;i++){

		
		printf("Case #%d: %d\n",i,getAmount());
	}

	return 0;
}