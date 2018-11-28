#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
void mm(char *str)
{
	int cc = 0;
	for(int lx =0;str[lx] != '\0';lx++)
		if(str[lx] != str[lx+1])
			str[cc++] = str[lx];
	str[cc] = '\0';
	return;
}
bool eq(char *s1,char *s2)
{
	if(strlen(s1) != strlen(s2)) return false;
	for(int lx = 0;s1[lx] != '\0';lx++)
	{
		if(s1[lx] != s2[lx])
			return false;
	}
	return true;
}
int main()
{
	int T;scanf("%d",&T);
	for(int lT = 1;lT <= T;lT++)
	{
		int k;scanf("%d",&k);
		char pair[101][101][2];
		memset(pair,0,101*101*2);
		int cnt[101];
		for(int lk = 0;lk < k;lk++)
		{
			char str[102];
			scanf("%s",str);
			int IV = 0;
			cnt[lk] = 0;
			for(int lx = 1; str[lx-1] != 0;lx++)
			{
				if((str[lx] != str[lx-1])){
					pair[lk][cnt[lk]][0] = str[lx-1];
					pair[lk][cnt[lk]][1] = lx - IV;
					cnt[lk]++;
					IV = lx;
				}
			}
		}

		bool isok = true;
		for(int lx = 1;lx < k;lx++)
			if(cnt[lx] != cnt[lx-1])
				isok = false;
		int step = 0;	
		for(int lx = 0;lx < cnt[0];lx++){
			int low = pair[0][lx][1], upp = pair[0][lx][1];
			for(int lk = 0;lk < k;lk++){
//				printf("%d))\n",pair[lk][lx][1]);
				if( low > pair[lk][lx][1])
					 low = pair[lk][lx][1];
				else if(upp < pair[lk][lx][1])
					 upp = pair[lk][lx][1];
				if((lk>0) and(pair[lk-1][lx][0] != pair[lk][lx][0])){
					isok = false;
					break;
				}
			}
//			printf("%d ~ %d\n",low,upp);
			step += (upp-low)*(k/2);
		}
		if(isok)
			printf("Case #%d: %d\n",lT,step);
		else
			printf("Case #%d: Fegla Won\n",lT);
	}
	return 0;
}
