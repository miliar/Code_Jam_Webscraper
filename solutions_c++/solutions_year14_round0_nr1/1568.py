#include <cstdio>

int main()
{
	int t, c = 1, ans, r, now, count;
	int table[2][4][4], inrow[17];
	scanf("%d", &t);
	while(t--){
		for(int i = 0;i < 17;i++)
			inrow[i] = 0;
		count = 0;
		for(int x = 0;x < 2;x++){
			scanf("%d", &r);
			for(int i = 0;i < 4;i++){
				for(int j = 0;j < 4;j++){
					scanf("%d", &now);
					if(x == 0 && i == r - 1){
						inrow[now] = 1;
					}else if(x == 1 && i == r - 1){
						if(inrow[now]){
							count++;
							ans = now;
						}
					}
				}
			}
		}
		if(count == 1)
			printf("Case #%d: %d\n", c++, ans);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n", c++);
		else
			printf("Case #%d: Volunteer cheated!\n", c++);
	}
	return 0;
}
