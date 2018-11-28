#include <cstdio>

bool insomnia(int have_seen[]){
	for(int i=0; i<10; i++){
		if(have_seen[i]==false) return true;
	}
	return false;
}

main(){
	int t,n,last,have_seen[10];

	scanf("%d", &t); //testcase
	for(int i=1; i<=t; i++){
		for(int j = 0; j<11; j++){
			have_seen[j] = false;
		}

		scanf("%d", &n); //input
		int j = 1, last = n;

		if(n!=0){
			while(insomnia(have_seen)==true){ //cont when insomnia == true
				last = n*j; // store last num
				int a = last;

				while(a!=0){ //check if have seen
					int mod = a%10;
					a = a/10;
					have_seen[mod] = true;

				}
				j++;
			}
			printf("Case #%d: %d\n", i,last);
		}
		else{
			printf("Case #%d: INSOMNIA\n", i);
		}
	}

}