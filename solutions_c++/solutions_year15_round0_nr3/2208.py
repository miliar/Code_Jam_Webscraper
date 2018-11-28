#include <iostream>
#include <string>
using namespace std;

#define I 4
#define J 17
#define K 112

int qdot(int a,int b)
{
	if(a<0)return -qdot(-a,b);
	if(b<0)return -qdot(a,-b);
	if(a==1)return b;
	if(b==1)return a;
	if(a==b)return -1;
	if(a==I)
	{
		if(b==J)return K;
		if(b==K)return -J;
	}
	if(a==J)
	{
		if(b==I)return -K;
		if(b==K)return I;
	}
	if(a==K)
	{
		if(b==I)return J;
		if(b==J)return -I;
	}
	cerr<<"strange a,b?"<<a<<"*"<<b<<endl;
	return 0;
}
int qinv(int a)
{
	if(a==1 || a==-1)return a;
	return -a;
}
int qpow(int a,int r)
{
	if(r>=4)return qpow(a,r%4);
	if(r<0){
		cerr<<"strange invocation: qpow"<<a<<","<<r<<endl;
		return qinv(qpow(a,-r));
	}
	switch(r)
	{
		case 0:return 1;
		case 1:return a;
		case 2:return qdot(a,a);
		case 3:return qdot(a,qdot(a,a));
	}
	cerr<<"strange branch: qpow"<<a<<","<<r<<endl;
	return 0;
}

string s;
int l,x;
int num[10010];
int cache[10010];
int lineprod;
void init()
{
	int prod=1;
	for(int i=0;i<l;i++)
	{
		int t=0;
		if(s[i]=='i')t=I;
		if(s[i]=='j')t=J;
		if(s[i]=='k')t=K;
		if(t==0){cerr<<"error input at pos:"<<i<<" of str"<<s<<endl;}
		prod=qdot(prod,t);
		num[i]=t;cache[i]=prod;
	}
	lineprod=prod;
}

int getprod(int pos)
{
	int line=pos/l, apos=pos%l;
	return qdot(cache[apos],qpow(lineprod,line));
}
int getnum(int pos)
{
	return num[pos%l];
}

string print(int a)
{
	if(a<0)return "-"+print(-a);
	switch(a)
	{
		case 1:return "1";
		case I:return "I";
		case J:return "J";
		case K:return "K";
	}
	return "ERR";
}	
	
int calc()
{
	cin>>l>>x;
	cin>>s;
	init();
	int allprod=qpow(lineprod,x);
	
	//for(int i=0;i<l;i++)
		//cerr<<print(cache[i])<<",";
	//cerr<<endl;
	//cerr<<"allprod:"<<print(allprod)<<endl;
	if(allprod!=qdot(I,qdot(J,K)))return -1;
	//cannot make it
	
	int i=0,stage=1,prod=1;
	for(;i<l*x-2;i++)
	{
		//cout<<"getprod "<<i<<print(getprod(i))<<endl;
		prod=qdot(prod,getnum(i));
		//cout<<"getprod "<<i<<print(prod)<<endl;
		
		if(prod==I){stage++;break;}
	}
	if(stage==1)return -1;
	
	for(i++;i<l*x-1;i++)
	{
		//cout<<"getprod "<<i<<print(getprod(i))<<endl;
		prod=qdot(prod,getnum(i));
		//cout<<"getprod "<<i<<print(prod)<<endl;
		
		if(prod==qdot(I,J)){stage++;break;}
	}
	if(stage==2)return -1;
	return 1;
}

int main()
{
	//cout<<calc();return 0;
	int N;cin>>N;
	for(int i=0;i<N;i++)
		cout<<"Case #"<<(i+1)<<": "<<(calc()>0?"YES":"NO")<<endl;
	return 0;
}