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
#define N 5
#endif

#ifdef small
#define N 5
#endif

#ifdef large1
#define N 16
#endif

#ifdef large2
#define N 102
#endif
typedef float decimal;
#define eps 1e-6
inline int comp(const decimal &a, const decimal &b) {
	if (fabs(a - b) < eps)
		return 0;
	else if(a<b){
		return -1;
	}
	else {
		return 1;
	}
}
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
int ispalindrome(char *a){
	int sizea=strlen(a);
	for(int i=0;i<=sizea/2;i++){
		if(a[i]!=a[sizea-i-1]){
			return 0;
		}
	}
	return 1;
}
	



void main(){

FILE *O,*I;
#ifdef none
freopen_s(&I,"ct.in","r+",stdin);
freopen_s(&O,"ct.out","w+",stdout);
#endif
#ifdef small
freopen_s(&I,"c-small-attempt0.in","r+",stdin);
freopen_s(&O,"c-small-attempt0.out","w+",stdout);
#endif

#ifdef large1
freopen_s(&I,"a-large-practice.in","r+",stdin);
freopen_s(&O,"a-large-practice.out","w+",stdout);
#endif
#ifdef large2
freopen_s(&I,"a-large-practice.in","r+",stdin);
freopen_s(&O,"a-large-practice.out","w+",stdout);
#endif

	int n,count=0;
	char minnum[N],maxnum[N],j[N]="1",product[2*N],temp[N];
	std::cin>>n;

	for(int i=1;i<=n;i++){
		count=0;
		std::cin>>minnum>>maxnum;
		strcpy(j,"1");
		multiply(product,2*N,j,j);
		int compare2=comp(product,maxnum);
		while(compare2==-1||compare2==0){
			int compare1=comp(product,minnum);
			if((compare1==1||compare1==0)&&ispalindrome(product)&&ispalindrome(j)){
				count++;
			}
			strcpy(temp,j);
			add(j,temp,"1");
			multiply(product,2*N,j,j);
			
		compare2=comp(product,maxnum);
		}
		std::cout<<"Case #"<<i<<": "<<count<<std::endl;
	}
	fclose(stdout);
	fclose(stdin);
}
