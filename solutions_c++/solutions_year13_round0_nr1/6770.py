
#include <iostream>
#include <vector>

#define DEBUG(...) \
        fprintf(stdout,__VA_ARGS__)


using namespace std;

enum resType {
        NONE,XWON,OWON,DRAW,GNCOM
};

class TicTacToe {

        char matrix[4][4];
        FILE * fip;
        FILE * fop;

        public:
        TicTacToe(char * file) { 
                fip = fopen(file,"r");
                fop = fopen("./output.txt","w");
                if (!fop || !fip) {
                        cerr << "Cannot open input/output file.!";
                        exit(1);
                }
        }

        void ReadMatrix();
        void PrintMatrix();
        resType ProcessMatrix();
        void ClearMatrix();

        ~TicTacToe() 
        { 
                if (fip) fclose(fip);
                fip = NULL;
                if (fop) fclose(fop);
                fop = NULL;
        }

};

void TicTacToe::ReadMatrix() {
        int T = 0;
        fscanf(fip,"%d\n",&T);
        DEBUG("Number of tests : %d\n",T);
        for (int t = 0; t < T; t++) {
                for(int i=0;i<4;i++) {
                        for(int j=0;j<4;j++) {
                                char ch = '\0';
                                fscanf(fip,"%c",&ch);
                                matrix[i][j] = ch;
                        }
                        fscanf(fip,"\n");
                }
                fscanf(fip,"\n");
                PrintMatrix();
                switch (ProcessMatrix()) {
                        case XWON: {
                                           fprintf(fop,"Case #%d: X won\n",t+1);
                                           DEBUG("Case #%d: X won\n",t+1);
                                   }
                                   break;
                        case OWON: {
                                           fprintf(fop,"Case #%d: O won\n",t+1);
                                           DEBUG("Case #%d: O won\n",t+1);
                                   }
                                   break;
                        case DRAW: {
                                           fprintf(fop,"Case #%d: Draw\n",t+1);
                                           DEBUG("Case #%d: Draw\n",t+1);
                                   }
                                   break;
                        case GNCOM: {
                                            fprintf(fop,"Case #%d: Game has not completed\n",t+1);
                                            DEBUG("Case #%d: Game has not completed\n",t+1);
                                    }
                                    break;
                        default:
                                    DEBUG("Incorrect result type.\n");
                }
        }

}


resType TicTacToe::ProcessMatrix() {
     resType res=  NONE;

     // X-ROW
     for(int i=0;i<4;i++) {
        int j = 0;
        for(;j<4;j++) {
           if ((matrix[i][j] != 'X') && (matrix[i][j] != 'T')) {
              break;
           }
        }
        if (j == 4) {
           return XWON;
        }
     }       
     // X-COL
     for(int j = 0;j<4;j++) {
        int i=0;
        for(;i<4;i++) {
           if ((matrix[i][j] != 'X') && (matrix[i][j] != 'T')) {
              break;
           }
        }
        if (i == 4) {
           return XWON;
        }
     }       
     // X-DIAG 1
     int i;
     for(i = 0;i<4;i++) {
           if ((matrix[i][i] != 'X') && (matrix[i][i] != 'T')) {
              break;
           }
     }
     if (i == 4) {
         return XWON;
     }       

     // X-DIAG 2
     for(i = 3;i>=0;i--) {
           if ((matrix[i][3-i] != 'X') && (matrix[i][3-i] != 'T')) {
              break;
           }
     }
     if (i < 0) {
         return XWON; 
     }       
        
     // O-ROW
     for(int i=0;i<4;i++) {
        int j = 0;
        for(;j<4;j++) {
           if ((matrix[i][j] != 'O') && (matrix[i][j] != 'T')) {
              break;
           }
        }
        if (j == 4) {
           return OWON;
        }
     }       

     // O-COL
     for(int j = 0;j<4;j++) {
        int i=0;
        for(;i<4;i++) {
           if ((matrix[i][j] != 'O') && (matrix[i][j] != 'T')) {
              break;
           }
        }
        if (i == 4) {
           return OWON;
        }
     }       
     // O-DIAG 1
     for(i = 0;i<4;i++) {
           if ((matrix[i][i] != 'O') && (matrix[i][i] != 'T')) {
              break;
           }
     }
     if (i == 4) {
         return OWON;
     }       

     // O-DIAG 2
     for(i = 3;i>=0;i--) {
           if ((matrix[i][3-i] != 'O') && (matrix[i][3-i] != 'T')) {
              break;
           }
     }
     if (i < 0) {
         return OWON;
     }       

     // Test for .
     for (i=0; i< 4;i++)
       for(int j=0;j<4;j++) 
          if (matrix[i][j] == '.')
              return GNCOM;

     return DRAW;
}

void TicTacToe::PrintMatrix() {
        cout << endl;
        for(int i=0;i<4;i++) {
                for(int j=0;j<4;j++) 
                        cout << matrix[i][j] << " ";
                cout << endl;
        }
}


int main (int argc,char *argv[]) {
        if (argc > 2) {
                fprintf(stderr,"Incorrect number of arguments.\n");
                exit(1);
        }

        TicTacToe obj(argv[1]);
        obj.ReadMatrix();
}














