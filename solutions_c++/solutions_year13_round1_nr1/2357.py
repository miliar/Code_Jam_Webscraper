#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <regex>
#include <algorithm>
#include <iomanip>

#define small
#ifdef none
#define N 10
#endif

#ifdef small
#define N 10
#endif

#ifdef large
#define N 1000
#endif

void add(char *a,char*b,char*c){
	int sizeb,sizec,carry=0,i;
	sizeb=strlen(b);
	sizec=strlen(c);
	int sizea,ptrb=sizeb-1,ptrc=sizec-1;
	if(sizeb>sizec){
		sizea=sizeb;
	}
	else {
		sizea=sizec;
	}
	a[sizea]='\0';

	for( i=sizea-1;i>=0&&ptrc>=0&&ptrb>=0;i--,ptrb--,ptrc--){
		a[i]=(char)((b[ptrb]+c[ptrc]+carry-2*(int)'0')%10+(int)'0');
		carry=(int)((b[ptrb]+c[ptrc]+carry-2*(int)'0')/10);
	}

	if(ptrb>-1){
		for(;ptrb>=0&&i>=0;i--,ptrb--){
			a[i]=(char)((int)(b[ptrb]+carry-(int)'0')%10+(int)'0');
			carry=(int)((b[ptrb]+carry-(int)'0')/10);
		}
	}
	else if(ptrc>-1){
		for(;ptrc>=0&&i>=0;i--,ptrc--){
			a[i]=(char)((int)(c[ptrc]+carry-(int)'0')%10+(int)'0');
			carry=(int)((c[ptrc]+carry-(int)'0')/10);
		}
	}
	if(carry!=0){
		int j=0;
		char temp=a[j],temp2;
		a[j]=(char)(carry+(int)'0');
		j++;
		for(;j<=sizea;j++){
			temp2=a[j];
			a[j]=temp;
			temp=temp2;
		}
		a[j]=temp;
	}
}
int multiply(char*a,int n,char*b,char*c){
	int sizeb,sizec,carry=0;
	sizeb=strlen(b);
	sizec=strlen(c);
	int sizea,ptrb=sizeb-1,ptrc=sizec-1;
	if(sizeb+sizec>n){
		a[0]='\0';
		return 0;
	}
	else {
		sizea=sizeb+sizec-1;
	}
	strcpy(a,"0");
	char temp[2][2*N];
	strcpy(temp[0],"0");
	
	for(int j=0;ptrb>=0;j++,ptrb--){
		temp[1][sizec+j]='\0';
		for(int k=j-1;k>=0;k--){
			temp[1][sizec+k]='0';
		}
		for(ptrc=sizec-1 ;ptrc>=0;ptrc--){
			int x=b[ptrb]-(int)'0';
			int y=c[ptrc]-(int)'0';
			temp[1][ptrc]=(char)((x*y) %10 +(int)'0');
			carry=(char)((x*y) /10 );
		}
		if(carry!=0){
			int f=0;
			char temp1=temp[1][f],temp2;
			temp[1][f]=(char)(carry+(int)'0');
			f++;
			for(;f<=sizec+j;f++){
				temp2=temp[1][f];
				temp[1][f]=temp1;
				temp1=temp2;
			}
			temp[1][f]=temp1;
		}

		add(a,temp[0],temp[1]);
		strcpy(temp[0],temp[1]);
	}
	return 1;
}
int comp(char *a,char *b){
	int sizea=strlen(a);
	int sizeb=strlen(b);
	if(sizea>sizeb)return 1;
	else if(sizea<sizeb)return -1;
	else{
		for(int i=0;i<sizea;i++){
			if(a[i]>b[i]){
				return 1;
			}
			else if(a[i]<b[i]){
				return -1;
			}
		}
		return 0;
	}
}

void increment(char *a){
	int sizea=strlen(a);
	int carry=(a[sizea-1]+1-(int)'0')/10;
	a[sizea-1]=(a[sizea-1]+1-(int)'0')%10+'0';

	int ptr=sizea-2;
	while(carry!=0){
		
		carry=(a[ptr]+1-(int)'0')/10;
		a[ptr]=(a[ptr]+1-(int)'0')%10+'0';
		ptr--;
		if(ptr<0)
			break;
		}
	if(carry!=0){
		int f=0;
		char temp1=a[f],temp2;
		a[f]=(char)(carry+(int)'0');
		f++;
		for(;f<=sizea;f++){
			temp2=a[f];
			a[f]=temp1;
			temp1=temp2;
		}
		a[f]=temp1;
	}
}
void main(){
FILE *o,*i;
#ifdef none
freopen_s(&i,"a.txt","r+",stdin);
freopen_s(&o,"a.out","w+",stdout);
#endif
#ifdef small
freopen_s(&i,"a-small-attempt0.in","r+",stdin);
freopen_s(&o,"a-small-attempt0.out","w+",stdout);
#endif

#ifdef large
freopen_s(&i,"a-large-practice.in","r+",stdin);
freopen_s(&o,"a-large-practice.out","w+",stdout);
#endif

	int n;
	long long p,r,t;
	//char r[50],t[50],p[50],m[50],l[50];
	
	std::cin>>n;

	for(int i=1;i<=n;i++){
		
			std::cin>>r>>t;
			long long k=sqrt((2*r-1)*(2*r-1)+8*t);
			p=(long long)((k)-2*r+1)/4;
			std::cout<<"Case #"<<i<<": "<<p<<std::endl;

	}
	
	fclose(stdout);
	fclose(stdin);

}
