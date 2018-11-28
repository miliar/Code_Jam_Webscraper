#include<iostream>
#include<cstdio>
#include<cstring>
#include<stack>
using namespace std;

int A[100];
int T,size;
string s;
stack<int> rstack1;
long long flipc=0;

void arrclr(){
	for(int i=0;i<100;i++)
		A[i]=2;
}

int findneglast(int size){
	int i;
	for(i=size-1;i>=0;i--){
		if(A[i]==0)
			break;
	}
	return i;
}
int findposlast(int point){
	int i;
	for(i=point-1;i>=0;i--){
		if(A[i]==1)
			break;
	}
	return i;
}
void flptrnsfm(int s_i){
	for(int i=0;i<=s_i;i++){
		int x=A[i];
		if(x==0)
			A[i]=1;
		if(x==1)
			A[i]=0;
		rstack1.push(A[i]);
	}
	for(int i=0;i<=s_i;i++){
		A[i]=rstack1.top();
		rstack1.pop();
	}
	flipc++;
}
int main(){
	scanf("%d\n",&T);
	for(int j=0;j<T;j++){
		flipc=0;
		cin>>s;
		for(int i=0;i<s.size();i++){
			if(s[i]=='+')
				A[i]=1;
			if(s[i]=='-')
				A[i]=0;
		}
		int ln=findneglast(s.size());
		while(ln>=0){
			int x=A[0];
			if(x==0){
				flptrnsfm(ln);
			}
			else{
				int y=findposlast(ln);
				flptrnsfm(y);
			}
			ln=findneglast(s.size());
		}
		cout<<"Case #"<<j+1<<": "<<flipc<<endl;
	}
	return 0;
}