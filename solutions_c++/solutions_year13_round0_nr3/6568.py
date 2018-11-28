#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;
int ispalindrome(int num) {
	int k,i,j;
	k=num;
	j=0;
	while(num!=0) {
		i=num%10;
		j=j*10+i;
		num/=10;
	}
	if(k==j) return 1;
	else return 0;
}
int main() {
	int t,a,b,temp;
	cin>>t;
	int ans[t];
	for(int i=0;i<t;i++) {
		cin>>a>>b;
		temp = (int)sqrt(a);
		if(temp*temp<a)
			temp++;
		ans[i]=0;
		while(1) {
			if(temp*temp<=b) {
				if(ispalindrome(temp)==1)
					if(ispalindrome(temp*temp)==1)
						ans[i]++;
				temp++;
			}
			else break;
		}
	}
	for(int i=0;i<t;i++)
		cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
	return 0;
}
