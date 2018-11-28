// By Aman Jain(jainaman224)
// 9/4/16

#include <iostream>

using namespace std;

int main(){
	int i,j,k,l,t,array[10]={0};
	long n,temp;
	cin >> t;
	for(i=1;i<=t;i++){
		cin >> n;
		if(n==0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else{
			k=1;
			j=0;
			while(j!=10){
				temp=k*n;
				k++;
				while(temp){
					array[temp%10]=1;
					temp /= 10;
				}
				j=0;
				for(l=0;l<10;l++){
					if(array[l]==1)
						j++;
				}
			}
			cout << "Case #" << i << ": " << (k-1)*n << endl;
			for(l=0;l<10;l++){
				array[l]=0;
			}
		}
	}
}