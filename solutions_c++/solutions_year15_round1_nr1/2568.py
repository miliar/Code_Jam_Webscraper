#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int test_cases, n, maximum_cookies, difference, a[1000];
	unsigned int minimum_1,minimum_2;
	cin>>test_cases;
	for(int j=1;j<=test_cases;j++){
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i];
		minimum_1=maximum_cookies=0;
		for(int i=0;i<n-1;i++){
			difference =a[i]-a[i+1];
			if(difference>0)
				minimum_1+=difference;
		}
		for(int i=0;i<n-1;i++){
			difference =a[i]-a[i+1];
			if(difference>maximum_cookies)
				maximum_cookies=difference;
		}
		minimum_2=0;
		for(int i=0;i<n-1;i++){
			if(a[i]>maximum_cookies)
				minimum_2+=maximum_cookies;
			else
				minimum_2+=a[i];
		}
		cout<<"Case #"<<j<<": "<<minimum_1<<" "<<minimum_2<<endl;
	}
}