#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

char input[10000];

int main()
{
	int t, caseNum = 1, ans, n, i, j, idx[101], c, len[101], flag, sum, avg, maxSize;
	char now;
	vector<int> count[101];
	vector<char> letter[101];
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		maxSize = -1;
		for(i = 0;i < n;i++){
			count[i].clear();
			letter[i].clear();
			scanf("%s", input);
			now = input[0];
			count[i].push_back(1);
			letter[i].push_back(now);
			for(j = 1;j < strlen(input);j++){
				if(now == input[j]){
					count[i][count[i].size()-1]++;
				}else{
					letter[i].push_back(input[j]);
					count[i].push_back(1);
					now = input[j];
				}
			}
			//printf("%d %d\n", letter[i].size(), maxSize);
			if((int)letter[i].size() > maxSize){
				maxSize = letter[i].size();
			}
		}
		/*for(i = 0;i < n;i++){
			for(j = 0;j < letter[i].size();j++)
				printf("%c %d ", letter[i][j], count[i][j]);
			printf("\n");
		}*/
		flag = 0;
		ans = 0;
		for(i = 0;i < maxSize;i++){
			sum = count[0][i];
			for(j = 1;j < n;j++){
				if(i >= letter[j].size() || letter[j][i] != letter[0][i]){
					flag = 1;
					break;
				}else
					sum += count[j][i];
			}
			if(flag == 1)
				break;
			avg = sum / n;
			if((double)sum / (double)n - avg > 0.5)
				avg++;
			for(j = 0;j < n;j++){
				ans += abs(count[j][i] - avg);
			}
		}
		if(flag == 1)
			printf("Case #%d: Fegla Won\n", caseNum++, ans);
		else
			printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
