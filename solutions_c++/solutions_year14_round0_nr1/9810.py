#include<cstdio>
int search_card();
int file1[4];
int file2[4];
int card = 0;
int main() {
    FILE *input = fopen("input.in","r");
    FILE *output = fopen ("ouput.out", "w");
    int cases,file;
    int matrix_cards[4][4];
    fscanf(input,"%d",&cases);
    for(int c=1;c<=cases;c++) {
        fscanf(input,"%d",&file);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fscanf(input,"%d",&matrix_cards[i][j]);
        for(int i=0;i<4;i++) file1[i] = matrix_cards[file-1][i];
        fscanf(input,"%d",&file);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fscanf(input,"%d",&matrix_cards[i][j]);
        for(int i=0;i<4;i++) file2[i] = matrix_cards[file-1][i];
        if(search_card() == -1) fprintf(output,"Case #%d: Volunteer cheated!\n",c);
        if(search_card() == 1) fprintf(output,"Case #%d: %d\n",c,card);
        if(search_card() > 1) fprintf(output,"Case #%d: Bad magician!\n",c);
    }
}
int search_card() {
    int cards = 0;
    for(int i=0;i<4;i++) {
        for(int j=0;j<4;j++) {
            if(file1[i] == file2[j]) {
                card = file1[i];
                cards++;
            }
        }
    }
    if(cards == 1) return 1;
    if(cards > 1) return cards;
    if(cards == 0) return -1;
}
