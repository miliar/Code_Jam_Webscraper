#include <iostream>

using namespace std;

int main () {
	int test, n, i, a[10], k, num, rem, flag = 0,ans;
	cin>>test;
	k = 1;
	while (test--) {

		cin>>n;
		for (i = 0; i < 10; i++) {
			a[i] = 0;
		}
		i = 1;
        if (n == 0) {
        	cout<<"Case #"<<k<<":"<<" "<<"INSOMNIA"<<"\n";
        } else {

        	while(flag != 10) {	
        		num = n*i;
        		ans = num;
        		while (num) {
        			rem = num%10;
        			num = num/10;
        			if (a[rem] == 0) {
        				a[rem] = 1;
        				flag = flag + 1;
        			}
        		}
        		i = i + 1;
        	}
        	cout<<"Case #"<<k<<":"<<" "<<ans<<"\n";
        }
        flag = 0;
        k++;
	}
	return 0;
}