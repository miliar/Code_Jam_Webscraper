#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int pre[200000], cnt = 0;
FILE *fp, *fw;

int main() {
	int i, j, k, fg, cse, g = 1, a, b, res;
	char tp[100];
	fp = fopen("/home/uriel/workspace/C-small-attempt0.in", "r");
	fw = fopen("/home/uriel/workspace/outC.txt", "w");
	for(i = 1; i <= 10000000; ++i) {
		j = i;
		k = 0;
		memset(tp, 0x00, sizeof(tp));
		while(j > 0) {
			tp[k++] = (j % 10) + '0';
			j /= 10;
		}
		fg = 0;
		for(j = 0; j <= strlen(tp) / 2; ++j) {
			if(tp[j] != tp[strlen(tp) - 1 - j]) {
				fg = 1;
				break;
			}
		}
		if(!fg) pre[cnt++] = i;
	}
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %d", &a, &b);
		res = 0;
		for(i = 0; i < cnt; ++i) {
			if(pre[i] * pre[i] >= a) break;
		}
		for(; i < cnt; ++i) {
			if(pre[i] * pre[i] >= a && pre[i] * pre[i] <= b) {
				j = pre[i] * pre[i];
				k = 0;
				memset(tp, 0x00, sizeof(tp));
				while(j > 0) {
					tp[k++] = (j % 10) + '0';
					j /= 10;
				}
				fg = 0;
				for(j = 0; j <= strlen(tp) / 2; ++j) {
					if(tp[j] != tp[strlen(tp) - 1 - j]) {
						fg = 1;
						break;
					}
				}
				if(!fg) res++;
			}
			else
				break;
		}
		fprintf(fw, "Case #%d: %d\n", g++, res);
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
