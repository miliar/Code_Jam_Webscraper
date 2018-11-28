#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

int t,l;
char s[5000],a[5000]; 

void work(){
	int i,h,t;
	scanf ("%s",s);
	l=strlen (s);
	h=2000;t=2000;
	a[h]=s[0];
	for (i=1;i<l;i++){
		 if (s[i]>=a[h])
		 	a[--h]=s[i];
		else a[++t]=s[i];
	}
	a[++t]='\0';
	printf ("%s\n",a+h);
}

int main(){
	//freopen ("a.in","r",stdin);
	//freopen ("a.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		work (); 
	}
	return 0;
}
