#include<iostream>
#include<fstream>

using namespace std;


int check(char *b,int len){
	for(int i=0;i<len;i++)
	if(b[i]!='-')return 0;
	return 1;
}

char * all(char * b){

	return b;
}



int answer(char a[],int len){
	int result=0;
	int tmp=0;
	if(len>1){
	for(int i=0;i<len-1;i++){
		if(a[i]!=a[i+1]){
			tmp=i;
			i=tmp;
			result++;
		}
	}}
	if(a[len-1]=='-')result++;
	return result;	
}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	char a[1000];
	int length;
	cin>>length;
	for(int i=0;i<length;i++){
		cin>>a;
		cout<<" Case #"<<i+1<<": "<<answer(a,strlen(a))<<'\n';
	}
}