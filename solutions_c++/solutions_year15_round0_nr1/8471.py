#include <cstdio>
#include <cstring>
//#include <string>
using namespace std;

int main() {
	// your code goes here
	int t,max,temp;
	long done,ans;
	scanf("%d",&t);
	
	for(int j = 0 ; j< t; j++){
		done = 0;
		ans=0;
		char str[1001];
		scanf("%d",&max);
		
		scanf("%s",str);
		//printf("%s",str);
		for(int i = 0 ; i<= max; i++){
			
			temp = str[i] - '0';
			
			if(done>=i)
			{
				done+=temp;
			}
			else{
				//printf("adding %d",(i-done));
				ans+=(i-done);
				done+=temp+(i-done);
			}
			
			}
			
		
		printf("Case #%d: %ld\n",j+1, ans);

	}
	return 0;
}