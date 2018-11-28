#include<stdio.h>
#include<stdlib.h>

int main(int argc, char** argv) {
	int t;		// test cases
	char in[1002];

	scanf("%d",&t);
	for(int ti=0;ti<t;++ti) {
        int smax;
        scanf("%d",&smax);
        scanf("%s",in); // read input
        int needed=0;   // result - how many frends are needed.
        int sum=0;  // sum already

        for(int i=0;i<=smax;++i) {
            if(sum<i) {    //
                needed+=(i-sum);
                sum=i;
            }
            sum+=in[i]-'0'; // update with people with i-th shyness level
        }
        printf("Case #%d: %d\n",ti+1,needed); // print result
	}
	return 0;
}
