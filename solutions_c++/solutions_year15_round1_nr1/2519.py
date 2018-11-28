#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out2","w",stdout);
	int test, n, max, diff, a[1000];
	unsigned int m1,m2;
	cin>>test;
	for(int j=1;j<=test;j++){
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i];
		m1=max=0;
		for(int i=0;i<n-1;i++){
			diff =a[i]-a[i+1];
			if(diff>0)
				m1+=diff;
		}
		for(int i=0;i<n-1;i++){
			diff =a[i]-a[i+1];
			if(diff>max)
				max=diff;
		}
		m2=0;
		for(int i=0;i<n-1;i++){
			if(a[i]>max)
				m2+=max;
			else
				m2+=a[i];
		}
		cout<<"Case #"<<j<<": "<<m1<<" "<<m2<<endl;
	}
}