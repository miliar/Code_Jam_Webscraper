#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>

using namespace std;

int T;
char S[2020];
int letter[15];
int ans[10];
bool flag;

const int number[10][5]={{14,0,7,6,-1},
                   {6,5,0,-1,-1},
                   {9,12,6,-1,-1},
                   {9,3,7,0,0},
                   {1,6,10,7,-1},
                   {1,4,11,0,-1},
                   {8,4,13,-1,-1},
                   {8,0,11,0,5},
                   {0,4,2,3,9},
                   {5,4,5,0,-1}};

bool Allused() {
    for(int i=0;i<15;++i) {
        if(letter[i]) return false;
    }
    return true;
}
void dfs() {
    if(Allused()) {
        flag = true;
        return;
    }
    for(int i=0;i<10;++i) {
        if(letter[number[i][0]]==0) continue;
        if(letter[number[i][1]]==0) continue;
        if(letter[number[i][2]]==0) continue;
        if(number[i][3]!=-1 && letter[number[i][3]]==0) continue;
        if(number[i][4]!=-1 && letter[number[i][4]]==0) continue;
        
        --letter[number[i][0]];
        --letter[number[i][1]];
        --letter[number[i][2]];
        if(number[i][3]!=-1) --letter[number[i][3]];
        if(number[i][4]!=-1) --letter[number[i][4]];
        
        ++ans[i];
        dfs();
        if(flag) return;
        --ans[i];
        
        if(number[i][3]!=-1) ++letter[number[i][3]];
        if(number[i][4]!=-1) ++letter[number[i][4]];
        ++letter[number[i][0]];
        ++letter[number[i][1]];
        ++letter[number[i][2]];
    }
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d\n",&T);
	for(int i=1;i<=T;++i) {
        memset(letter,0,sizeof(letter));
        memset(ans,0,sizeof(ans));
        flag = false;
		gets(S);
        for(int j=strlen(S)-1;j>=0;--j) {
            switch(S[j]) {
                case 'E':++letter[0];break;
                case 'F':++letter[1];break;
                case 'G':++letter[2];break;
                case 'H':++letter[3];break;
                case 'I':++letter[4];break;
                case 'N':++letter[5];break;
                case 'O':++letter[6];break;
                case 'R':++letter[7];break;
                case 'S':++letter[8];break;
                case 'T':++letter[9];break;
                case 'U':++letter[10];break;
                case 'V':++letter[11];break;
                case 'W':++letter[12];break;
                case 'X':++letter[13];break;
                case 'Z':++letter[14];break;
            }
        }
        dfs();
        printf("Case #%d: ",i);
        for(int j=0;j<10;++j) {
            for(int k=0;k<ans[j];++k)
                printf("%d",j);
        }
        printf("\n");
	}
	return 0;
}

