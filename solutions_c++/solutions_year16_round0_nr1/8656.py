#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t;
	cin>>t;
	long long int n;
	long long int a[10];
	long long int tmp,z,tmp1,count,flag;
	for(long long int x = 1;x<=t;x++){
		cin>>n;
		flag = 0;
		count = 1;
		for(long long int i =0;i<10;i++)
			a[i] = 0;
			
		while(1){
			if(n==0){
				flag = 1;
				break;
			}
			tmp = n;
			tmp = tmp*count;
			tmp1 = tmp;
			while(tmp!=0){
				z = tmp%10;
				tmp/=10;
				a[z]+= 1;
			}
			count+=1;
			if(a[0]>=1&&a[1]>=1&&a[2]>=1&&a[3]>=1&&a[4]>=1&&a[5]>=1&&a[6]>=1&&a[7]>=1&&a[8]>=1&&a[9]>=1){
				flag = 2;
				break;
			}
			if(count >=200){
				flag = 1;
				break;
			}
		}
		if(flag == 1){
			cout<<"Case #"<<x<<": INSOMNIA\n";
		}else if(flag == 2){
			cout<<"Case #"<<x<<": "<<tmp1<<endl;
		}
	}	
	return 0;
}