    #include <bits/stdc++.h>
    using namespace std;
     
    int main() {
    	int test;
    	scanf ("%d", &test);
    	int a;
    	for (a = 1; a <= test; a++) {
    		long long int num;
    		scanf("%lld",&num);
    		map<int , int > mp;
    		int count = 0 ;
    		long long int temp;
    		long long int dg;
    		long long int ctr = 1;
    		long long 	int j = 0 ;
    		for (temp = num; 1; temp = ctr * num) {
    			count = 0 ;
    			while (temp) {
    				dg = temp % 10;
    				temp = temp/10;
    				mp[dg]++;
    			}
     
    			for (j = 0; j < 10; j++) {
    				if(mp[j] == 0){
    					count++;
    					break;
    				}
    			}
    			//printf("%d\n", count);
    			if (count == 0) {
    				printf("Case #%d: %lld\n",a, ctr*num);
    				break;
    			}else {
    				if (ctr*num > 100000000000000000 || ctr*num == 0){
    					printf("Case #%d:INSOMNIA\n", a);
    					break;
    				}
    			}
     
    			ctr++;
    		}
     
    		mp.clear();
    	}
    	return 0;
    }
