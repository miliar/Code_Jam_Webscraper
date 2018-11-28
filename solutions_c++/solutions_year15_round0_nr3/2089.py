#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fp, *fw;
char s[10010];

//void DFS(char *s) {
//	if(strlen(s) > 2) {
//		char s1[10010], s2[10010];
//		strcpy(s1, s);
//		s1[strlen(s) / 2] = '\0';
//		//printf("s1=%s\n", s1);
//		strcpy(s2, &s[strlen(s) / 2]);
//		//printf("s2=%s\n", s2);
//		DFS(s1);
//		DFS(s2);
//	}
//	else if(strlen(s) == 2) {
//	}
//	return;
//}

int main() {
	fp = fopen("D:\\GCJ\\C-small-attempt2.in", "r");
	//fp = fopen("D:\\GCJ\\in.txt", "r");
	fw = fopen("D:\\GCJ\\outCS.txt", "w");
	int cse, i, g = 1, n, l, res, cnt, maxa, fg, pos;
	char d[200][200], f[200][200];
	char str[10010], tp;
	memset(d, 0, sizeof(d));
	
	d['1']['1'] = '1'; d['1']['i'] = 'i'; d['1']['j'] = 'j'; d['1']['k'] = 'k';
	d['i']['1'] = 'i'; d['i']['i'] = '1'; d['i']['j'] = 'k'; d['i']['k'] = 'j';
	d['j']['1'] = 'j'; d['j']['i'] = 'k'; d['j']['j'] = '1'; d['j']['k'] = 'i';
	d['k']['1'] = 'k'; d['k']['i'] = 'j'; d['k']['j'] = 'i'; d['k']['k'] = '1';

	f['1']['1'] = 1; f['1']['i'] = 1; f['1']['j'] = 1; f['1']['k'] = 1;
	f['i']['1'] = 1; f['i']['i'] = -1; f['i']['j'] = 1; f['i']['k'] = -1;
	f['j']['1'] = 1; f['j']['i'] = -1; f['j']['j'] = -1; f['j']['k'] = 1;
	f['k']['1'] = 1; f['k']['i'] = 1; f['k']['j'] = -1; f['k']['k'] = -1;

	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %d", &l, &n);
		fscanf(fp, "%s", str);
		memset(s, 0x00, sizeof(s));
		for(i = 0; i < n; ++i) {
			strcat(s, str);
		}
		pos = 0;
		fg = 1;
		for(i = 0; i < n * l - 1; ++i) {
			//printf("%s\n", &s[i]);
			if(s[i] == 'i' && fg == 1 && pos == 0) {
				++pos;
				continue;
			}
			if(s[i] == 'j' && fg == 1 && pos == 1) {
				++pos;
				continue;
			}
			fg = f[s[i]][s[i + 1]] * fg;
			tp = d[s[i]][s[i + 1]];
			s[i + 1] = tp;
		}
		if(s[i] == 'k' && pos == 2 && fg == 1) fprintf(fw, "Case #%d: YES\n", g++);
		else
			fprintf(fw, "Case #%d: NO\n", g++);
	}
	fclose(fp);
	fclose(fw);
	system("PAUSE");
	return 0;
}
