#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

__int64  isPrime(__int64 p)
{      
 __int64 i;
 for (i=2;i<=sqrt((double)p);i++)
 {
    if(p%i==0)
     return i ;
 }
     return 0 ;      
}


int check(char *b,int len){
	for(int i=0;i<len;i++)
	if(b[i]!='-')return 0;
	return 1;
}

char * all(char * b){

	return b;
}

__int64 matanswer(int form,char *a,int len){
	__int64 tmp=0,smp=0;
	for(int i=1;i<len;i++){
		if(a[len-i-1]-48==1){
			smp =1;
			for(int k=0;k<i;k++)
				smp*=form;
		}
		else smp=0;
			tmp+=smp;
		}
	if(a[len-1]-48==1)
		tmp+=1;
	smp=isPrime(tmp);
	if(smp==0)return 0;
	else return smp;
}


int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	char a[17]="1000000000000001";
	int length,N,J;//,N=6,J=3;
	a[0]=a[15]='1';
	short count=0;
	__int64 result[9];
	int lv=0;
	int ac;//=N-2;
	cin>>length;
	cin>>N>>J;
	cout<<" Case #1: \n";
	while(lv<J){
		ac=N-2;
		for(int i=0;i<9;i++){
		count=1;
		result[i]=matanswer(i+2,a,strlen(a));
		if(result[i]==0){
			count=0;
		break;}
		}
		if(count==1){
			cout<<a<<" ";
			for(int i=0;i<9;i++)cout<<result[i]<<" ";
			cout<<"\n";
			lv++;
		}
		while(ac>0)
		if(a[ac]-48==1){
			a[ac]='0';
			ac-=1;
		}
		else{
			a[ac]='1';
			break;
		}


	}

}