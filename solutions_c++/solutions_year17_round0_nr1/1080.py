// 2017CodeJam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
using namespace std;

char str[1005];
int main(){
	freopen("D:\\A-large.in", "r+", stdin);
	freopen("D:\\output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);

	for (int cases = 1; cases <= T; cases++){
		printf("Case #%d: ", cases);
		int plen,slen,cnt=0;
		scanf("%s%d", str, &plen);
		slen = strlen(str);
		for (int i = 0; i < slen-plen; i++){
			if (str[i] == '+'){
				continue;
			}
			cnt++;
			for (int j = 0; j < plen; j++){
				if (str[i + j] == '-'){
					str[i + j] = '+';
				}
				else{
					str[i + j] = '-';
				}
			}
		}
		int ret = 0;
		for (int i = slen - plen; i < slen; i++){
			if (str[i] != str[slen - plen]){
				ret = 1;
				break;
			}
		}
		if (ret){
			printf("IMPOSSIBLE\n");
		}
		else{
			if (str[slen - plen] == '-'){
				cnt++;
			}
			printf("%d\n", cnt);
		}
	}
	//system("pause");
}