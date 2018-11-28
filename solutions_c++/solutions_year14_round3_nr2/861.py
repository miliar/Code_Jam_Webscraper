#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char car[11][105], result[10500], tmp[105];

int check(char s[], int n)
{
	int app[26] = {0};
	app[s[0] - 'a'] = 1;
	for(int i = 1;i < n;i++){
		if(app[s[i] - 'a'] == 1 && s[i] != s[i - 1])
			return 0;
		app[s[i] - 'a'] = 1;
	}
	return 1;
}

int dfs(int per[], int x, int n, int used[], int idx)
{
	int app[26] = {0}, flag;
	int ans = 0, i, j;
	char pre;
	if(x == n){
		idx = 0;
		/*app[car[per[0]][0] - 'a'] = 1;
		flag = 1;*/
		for(i = 0;i < n;i++){
			for(j = 0;j < strlen(car[per[i]]);j++){
				result[idx++] = car[per[i]][j];
				/*if(j == 0)
					pre = car[per[i-1]][strlen(car[per[i-1]]) - 1];
				else
					pre = car[per[i]][j - 1];
				if(app[car[per[i]][j] - 'a'] == 1 && car[per[i]][j] != pre){
					flag = 0;
					break;
				}
				app[car[per[i]][j] - 'a'] = 1;*/
			}
			//if(flag == 0)
				//break;
		}
		result[idx] = 0;
		//return flag;
		//printf("%d %s\n", idx, result);
		if(check(result, idx))
			return 1;
	}else{
		for(i = 0;i < n;i++){
			if(used[i] == 0){
				per[x] = i;
				used[i] = 1;
				for(int k = x;k < x + 1;k++){
					for(j = 0;j < strlen(car[per[k]]);j++){
						result[idx+j] = car[per[k]][j];
					}
				}
				if(check(result, idx + strlen(car[per[x]])))
					ans += dfs(per, x + 1, n, used, idx + strlen(car[per[x]]));
				used[i] = 0;
			}
		}
	}
	return ans;
}

int main()
{
	int t, caseNum = 1, ans, n, i, idx, j;
	int per[10], used[10];
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i = 0;i < n;i++){
			per[i] = i;
			used[i] = 0;
			scanf("%s", tmp);
			car[i][0] = tmp[0];
			idx = 1;
			for(j = 1;j < strlen(tmp);j++){
				if(tmp[j] != tmp[j - 1])
					car[i][idx++] = tmp[j];
			}
			car[i][idx] = 0;
		}
		ans = 0;
		for(i = 0;i < n;i++){
			per[0] = i;
			used[i] = 1;
			ans += dfs(per, 1, n, used, 0);
			used[i] = 0;
		}
		/*
		do{
			idx = 0;
			for(i = 0;i < n;i++){
				for(j = 0;j < strlen(car[per[i]]);j++)
					result[idx++] = car[per[i]][j];
			}
			result[idx] = 0;
			//printf("%d %s\n", idx, result);
			if(check(result, idx))
				ans++;
		}while(next_permutation(per, per + n));*/
		printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
