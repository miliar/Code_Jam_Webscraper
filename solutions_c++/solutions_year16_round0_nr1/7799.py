#include <iostream>
using namespace std;

int main() {
	int t,l;
	cin >> t;
	l=t;
	while(t--){
		long long n,k,p,flag=0,j=1;
		cin >> n;
		int a[10]={0};
		if(n==0)
		cout << "Case #" << l-t <<": INSOMNIA" << endl;
		else{
			while(flag==0){
		k = n*j++;
		p = k;
			while(k){
				a[k%10]=1;
				k=k/10;
			}
			flag=1;
			for(int i=0;i<10;i++ ){
				if(a[i]!=1)
				flag=0;
			}
			
			}
			cout << "Case #" << l-t << ": "<< p << endl;
		}
		
	}
	return 0;
}