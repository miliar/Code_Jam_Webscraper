#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
const int g[5][5]={
	0,0,0,0,0,
	0,1,2,3,4,
	0,2,-1,4,-3,
	0,3,-4,-1,2,
	0,4,3,-2,-1};
int a[10240];
inline int mul(int a, int b){
	if (a*b<0) return -mul(a,-b);
	else return g[abs(a)][abs(b)];
}
inline int divide(int p,int a){
	if (p*a<0) return -divide(p,-a);
	p=abs(p);
	a=abs(a);
	for (int i=1;i<=4;i++){
		if (g[a][i]==p)
			return i;
		else if (g[a][i]==-p)
			return -i;
	}
	return 0;
}
int main(){
	int t;
	cin >> t;
	int x,l;
	string s;
	int P;
	for (int ti=0;ti<t;ti++){
		cin >> l >> x;
		cin >> s;
		for (int i=0;i<l;i++)
			a[i]=s[i]-'i'+2;
		P=a[0];
		for (int i=1;i<l;i++)
			P=mul(P,a[i]);
		for (int i=1,j=0;i<x;){
			a[i*l+j]=a[j];
			P=mul(P,a[j]);
			j++;
			if (j>=l) { j=0; i++; }
		}
		/*
		for (int i=1;i<x;i++)
			memcpy(a+i*l,a,l*sizeof(int));
		*/
		/*
		for (int i=0;i<l*x;i++)
			cout << a[i];
		cout << endl;
		cout << "P=" << P <<endl;
		*/
		bool flag=false;
		for (int i=0,p1=a[0];i<l*x-2;i++,p1=mul(p1,a[i]))
			for (int j=i+1,p2=a[i+1];
				j<l*x-1;
				j++,p2=mul(p2,a[j])){
				int p3=divide(P,mul(p1,p2));
				//cout << "testing... " << i << " " << j << " p "	<< p1 << " " << p2 << " " << p3 << endl;
				if (
					((p1==2) && (p2==3) && (p3==4))
					){
					flag=true;
					break;
				}
			}
		cout << "Case #" << ti+1 << ": " << (flag?"YES":"NO") << endl;
	}
	return 0;
}