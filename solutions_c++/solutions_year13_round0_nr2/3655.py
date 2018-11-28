#include<stdio.h>

void startTheLogic(FILE *fp, int round) {

    char newline;
    int m , n, d;
    fscanf(fp, "%d", &m);    
    fscanf(fp, "%d", &n);    
    fscanf(fp, "%c", &newline);
    int array[m][n];
    bool success = true;
    for(int i =0 ; i< m; i++) {
        for(int j=0; j< n; j++) {
        fscanf(fp, "%d", &d);
        array[i][j] = d;
        }
        fscanf(fp,"%c", &newline);
        
       }

     int rowmin[m];
     int columnmin[n];

     for(int i =0 ; i< m ; i++) {
        rowmin[i] = array[i][0];
        for(int j =0; j< n ; j++)
         if(array[i][j] > rowmin[i] ) {
                rowmin[i] = array[i][j];
        }
     }
     
    for(int i =0 ; i<n  ; i++) {
        columnmin[i] = array[0][i];
        for(int j =0; j< m ; j++)
         if(array[j][i] > columnmin[i] ) {
                columnmin[i] = array[j][i];
        }
     }

     
    /*for(int i =0 ; i< m; i++) {
        for(int j=0; j< n; j++) {

        printf("%d ", array[i][j]);
     }
        printf("\n");
        }*/
 
    for(int i =0 ; i< m; i++) {
        for(int j=0; j< n; j++) {

        if((array[i][j] == rowmin[i]) ||  (array[i][j] == columnmin[j])) continue;
        else { success = false; printf("Case #%d: NO\n", round); break; }

        }  

        if(!success) break;

   }
        if(success) { 
            printf("Case #%d: YES\n", round);
        } 
}

int main() {

    FILE *fp = fopen("input.txt","r");
    int input;
    char newline;
    fscanf(fp, "%d", &input);
    fscanf(fp, "%c", &newline);
    int i =1;
    while(input > 0) {

        startTheLogic(fp, i++);
        --input;
    }


}
