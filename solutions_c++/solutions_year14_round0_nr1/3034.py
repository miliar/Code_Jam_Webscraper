#include <cstdio>
#include <cstring>

using namespace std;

int nums[20];
int nums2[20];
int in[4];


int main() {
	
	int T;
	scanf("%d", &T);
	
	for(int k = 1; k <= T; k++) {
		memset(nums, 0, sizeof(nums));
		memset(in, 0, sizeof(in));
		memset(nums2, 0, sizeof(nums2));
		
		int r;
		
		scanf("%d", &r);
		
		for(int i = 1; i <= r; i++) {
			scanf("%d %d %d %d", in, in+1, in+2, in+3);
		}
		
		for(int i = 0; i < 4; i++) nums[in[i]] = 1;
		
		for(int i = r+1; i <= 4; i++) {
			scanf("%d %d %d %d", in, in, in, in);
		}
		
		scanf("%d", &r);
		
		for(int i = 1; i <= r; i++) {
			scanf("%d %d %d %d", in, in+1, in+2, in+3);
		}
		
		for(int i = 0; i < 4; i++) {
			nums2[in[i]] = 1;
		}
		
		for(int i = r+1; i <= 4; i++) {
			scanf("%d %d %d %d", in, in, in, in);
		}
		
		int ans = -1;
		int n = 0;
		
		for(int i = 1; i <= 16; i++) {
			if(nums[i]&nums2[i]) {
				n++;
				ans = i;
			}
		}
		
		printf("Case #%d: ", k);
		
		if(n == 0) printf("Volunteer cheated!\n");
		else if(n == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}
	
	return 0;
}
