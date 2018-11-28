#include <stdio.h>
#include <string.h>

int char_cnt(char s[], char c){
    int cnt = 0;
    for(int i=0; i<strlen(s); i++)
        if(s[i] == c)
            cnt++;
    return cnt;
}

int main(){
    int X[26][10];
    for(int i=0; i<26; i++)
        for(int j=0; j<10; j++)
            X[i][j] = 0;
    X['Z'-'A'][0]++;
    X['E'-'A'][0]++;
    X['R'-'A'][0]++;
    X['O'-'A'][0]++;
    X['O'-'A'][1]++;
    X['N'-'A'][1]++;
    X['E'-'A'][1]++;
    X['T'-'A'][2]++;
    X['W'-'A'][2]++;
    X['O'-'A'][2]++;
    X['T'-'A'][3]++;
    X['H'-'A'][3]++;
    X['R'-'A'][3]++;
    X['E'-'A'][3]++;
    X['E'-'A'][3]++;
    X['F'-'A'][4]++;
    X['O'-'A'][4]++;
    X['U'-'A'][4]++;
    X['R'-'A'][4]++;
    X['F'-'A'][5]++;
    X['I'-'A'][5]++;
    X['V'-'A'][5]++;
    X['E'-'A'][5]++;
    X['S'-'A'][6]++;
    X['I'-'A'][6]++;
    X['X'-'A'][6]++;
    X['S'-'A'][7]++;
    X['E'-'A'][7]++;
    X['V'-'A'][7]++;
    X['E'-'A'][7]++;
    X['N'-'A'][7]++;
    X['E'-'A'][8]++;
    X['I'-'A'][8]++;
    X['G'-'A'][8]++;
    X['H'-'A'][8]++;
    X['T'-'A'][8]++;
    X['N'-'A'][9]++;
    X['I'-'A'][9]++;
    X['N'-'A'][9]++;
    X['E'-'A'][9]++;
    int XtX[10][10];
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            XtX[i][j] = 0;
            for(int k=0; k<26; k++)
                XtX[i][j] += X[k][i]*X[k][j];
        }
    }
    int ad[10][10];
    FILE *fp = fopen("ad.csv","r");
    for(int i=0; i<10; i++)
        for(int j=0; j<10; j++)
            fscanf(fp,"%d",&ad[i][j]);
    fclose(fp);
    int det=10400;
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
		char S[2010];
		scanf(" %s",S);
        int cnt[26];
        for(int i=0; i<26; i++)
            cnt[i] = char_cnt(S,'A'+i);
        int Xty[10];
        for(int i=0; i<10; i++){
            Xty[i] = 0;
            for(int j=0; j<26; j++)
                Xty[i] += X[j][i]*cnt[j];
        }
        int digits[10];
        for(int i=0; i<10; i++){
            digits[i] = 0;
            for(int j=0; j<10; j++)
                digits[i] += ad[i][j]*Xty[j];
            digits[i] /= det;
        }
		printf("Case #%d: ",t+1);
        for(int i=0; i<10; i++)
            for(int j=0; j<digits[i]; j++)
                printf("%d",i);
		printf("\n");
	}
	return 0;
}
