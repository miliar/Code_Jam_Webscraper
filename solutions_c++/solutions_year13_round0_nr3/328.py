#include<cstdio>
#include<cstdlib>
#include<string>
#include<iostream>
using namespace std;
string fun(string s) {
	string tmp;
	char plus[10];
	int num[200]={0};
	int val[300]={0};
	int len=s.length(),i,j;
	for(i=0;i<len;i++) num[i]=s[i]-48;
	for(i=0;i<len;i++) 
		for(j=0;j<len;j++)
			val[i+j]+=num[i]*num[j];			
	for(i=0;i<len*2-1;i++) {
		val[i+1]+=val[i]/10;
		val[i]%=10;
		tmp+=(char)(val[i]+48);
	}
	if(val[len*2-1]>0) 	{
		itoa(val[len*2-1],plus,10);
		tmp+=(string)plus;
	}
	return tmp;
}
bool fum(string s) {
	int len=s.length();
	for(int i=0;i<len/2;i++)
		if(s[i]!=s[len-i-1]) return false;
	return true;
}
bool more(string a,string b) {
	int la=a.length();
	int lb=b.length();
	if(la>lb) return true;
	if(la<lb) return false;
	for(int i=0;i<la;i++) {
		if(a[i]>b[i]) return true;
		if(a[i]<b[i]) return false; }
	return false;
}
int main () {
	int i,a=3,b=3,j;
	int t,T;
	string n,m;
	string A[50000];
	string B[50000];
	string op[3];
	string tmp,val,C;
	A[0]="1";A[1]="2";A[2]="3";
	B[0]="1";B[1]="4";B[2]="9";
	op[0]="0";op[1]="1";op[2]="2";
	for(i=0;;i++) {
		if(B[i].length()>100) break;
		//cout << A[i]<< " " << B[i] << endl;
		for(j=0;j<3;j++) {
			C=A[i];
			tmp=C.insert(C.length()/2,op[j]);
			val=fun(tmp);
			if(fum(val)) {
				A[a++]=tmp; B[b++]=val;
			}
		}
	}
	scanf("%d",&T);
	for(t=0;t<T;t++) {
		cin >> n >> m;
		for(i=0;more(n,B[i])&&i<b;i++) {}
		for(j=b-1;more(B[j],m)&&j>=0;j--) {}
		printf("Case #%d: %d\n",t+1,j-i+1);
	}
	return 0;
}