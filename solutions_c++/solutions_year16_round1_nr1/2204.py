#include<iostream>
#include <stdio.h>
#include<string.h>

using namespace std;

int main (){
	
	freopen("in.txt", "r", stdin);
	freopen("out-l.txt", "w", stdout);
	int t, i, j, k, z, l;
	char a[10000], b, c[10000], d[10000];
	cin>>t;
	for (i=0;i <t;i++){
		z=1;
		k=1;
		cin>>a;
		l = strlen(a);
		b = a[0];

		for(j=1;j <l;j++){
			if (a [j]>=b){
				c [k++]=a[j];
				b=a [j];
			}
			else if (a [j]<b)
				d [z++]=a [j];
		}
		cout<<"Case #"<<i+1<<": ";
		k--;
		z--;
		for (j=k;j>=1;j--)
			cout<<c[j];
		cout<<a[0];
		for (j=1;j <=z;j++)
			cout<<d[j];
		cout<<endl;
	}
	return 0;

}
