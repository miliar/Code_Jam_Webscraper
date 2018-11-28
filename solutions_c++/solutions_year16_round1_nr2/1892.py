#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<algorithm>
using namespace std;
int main() {
	int t,i;
	scanf("%d",&t);
	string str;
	for(int x=1;x<=t;x++) {
		scanf("%d",&i);
		int a[((2*i)-1)*i];
		int temp;
		for(int j=0;j<((2*i)-1)*i;j++) {
			scanf("%d",&temp);
			a[j]=temp;
		}
		int res[i];
		int n=(((2*i)-1)*i);
		sort(a,a+(((2*i)-1)*i));
		int tmp=a[0],c=0;
		int check=0;
		for(int j=0;j<n;j++) {
			if(check==a[j]) {
				continue;
			}
			check=a[j];
			int count=0;
			for(int k=0;k<n;k++) {
				if(a[j]==a[k]) {
					count++;
				}
			}
			if(count%2!=0) {
				res[c]=a[j];
				c++;
			}
		}
		sort(res,res+i);
		cout<<"CASE #"<<x<<": ";
		for(int k=0;k<i;k++) {
			cout<<res[k]<<" ";
		}
		cout<<endl;
		
	}
}
