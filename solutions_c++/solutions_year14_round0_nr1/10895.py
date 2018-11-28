#include<cstdio>
#include<cstdlib>

using namespace std;

int main() {
	FILE *fin = fopen("a.in","r"), *fout = fopen("a.out","w");
    int cases;

	fscanf(fin,"%d",&cases);
	for (int q = 0 ; q<cases ; q++){

        int choiceOne,choiceTwo,a,ret=-1;
        int gameOne[ 4 ][ 4 ];
        int gameTwo[ 4 ][ 4 ];
        bool mapper [17];
        bool found,bad = false;

        for(int i= 0; i<17; i++){
            mapper[i] = false;
        }

        fscanf(fin,"%d",&choiceOne);
        for(int i= 0; i<4; i++){
            for(int j= 0; j<4; j++){
                fscanf(fin,"%d",&a);
                gameOne[i][j] = a ;
            }
        }

        for(int i= 0; i<4; i++){
            mapper[gameOne[choiceOne-1][i]] = true;
        }

        fscanf(fin,"%d",&choiceTwo);
        for(int i= 0; i<4; i++){
            found = false;
            for(int j= 0; j<4; j++){
                fscanf(fin,"%d",&a);
                gameTwo[i][j] = a ;

                if (i == choiceTwo-1){
                    if (mapper[a]){
                        mapper[a] = false;
                        if (found){
                            bad = true;
                        }
                        ret = a;
                        found = true;
                    }
                }
            }
        }

        if (bad){
            fprintf(fout,"Case #%d: Bad magician!\n",q+1);
        } else if (ret == -1){
            fprintf(fout,"Case #%d: Volunteer cheated!\n",q+1);
        } else {
            fprintf(fout,"Case #%d: %d\n",q+1, ret);
        }
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
