#include <iostream>
using namespace std;
long int l=1;
int main() {
	long int t;
	cin >> t;
	while(t--) {
	    long long int n=0,temp=0,i=0,j=0,cnt=0,x=0,result=0,a[10]={0};
	    cin >> n;
	    if(n==0) {cout <<"Case #"<<l<<": "<<"INSOMNIA"<<endl;}
	    else {
	        temp = n;
	        for(i=1;i<=10000;i++) {
	            result=temp = i*n;
    	        while(temp!=0) {
    	            x = temp%10;
    	            a[x] = 1;
    	            temp /=10;
    	        }
    	        for(j=0;j<10;j++) {if(a[j]==1)cnt++;}
    	        if(cnt==10){break;}else{cnt=0;}
	        }
	        cout <<"Case #"<<l<<": "<<result<<endl;
	    }
	    l++;
	}
	return 0;
}
