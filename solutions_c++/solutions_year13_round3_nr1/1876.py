#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;



char L[150];

int con(char s){


	if(s=='a' || s=='e' || s=='i' || s=='o' || s=='u')
		return 0;
	return 1;

}

int check1(int s,int l, int n){

	int t=1,i;

	for(i=s; i<l;i++){

		if(con(L[i]))
			break;
	}

	if(t!=n)
		return 0;

	return l-i;

}

int check(int s,int l, int n){

	int t=1,i;

	for(i=s; i<l-1;i++){

		if(con(L[i]) && con(L[i+1])){
			t++;
			if(t==n)
			break;
		}
		else
			t=1;


	}

	if(t!=n)
		return 0;

	return l-i-1;

}



int main(){


//freopen("A-small-attempt0.in","r",stdin);
//freopen("A-small-attempt0.out","w",stdout);


	int T,ans,i,j,n,l;


	scanf("%d",&T);

	for(i=1;i<=T;i++){
		getchar();;
		scanf("%s%d",L,&n);

		l=strlen(L);

		ans=0;

		if(n>1){

			for(j=0;j<l;j++){

				ans+=check(j,l,n);
	
			}
		}

		else{
			for(j=0;j<l;j++){

			ans+=check1(j,l,n);
	
			}
		}
		
		printf("Case #%d: %d\n",i,ans);

	}
	 
    return 0;
}