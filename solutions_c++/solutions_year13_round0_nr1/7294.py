#include<iostream>
#include<fstream>
#include<string>
using namespace std;

class TicTacToeTomek {
  private:
    int dataSet;
    char input[1000][4][4];
    string output[1000];
  public:
    void readFromFile(char* fileName) {
        ifstream in;
        in.open(fileName);
        in >> dataSet;
        for(int k=0; k<dataSet; k++) for(int i=0; i<4; i++) for(int j=0; j<4; j++) in >> input[k][i][j];
        in.close();
    }

    void writeToFile(char* fileName) {
        ofstream out;
        out.open(fileName);
        for(int k=0; k<dataSet; k++) out << "Case #" << k+1 << ": " << output[k] << endl;
        out.close();
    }

    void compute() { for(int k=0; k<dataSet; k++)
        for(int l=0; l<4; l++) {
            int x=0, o=0;
            for(int j=0; j<4; j++)
                if(input[k][l][j]=='.') break;
                else if(input[k][l][j]=='T') { x++; o++; }
                else if(input[k][l][j]=='X') x++;
                else if(input[k][l][j]=='O') o++;
            if(x==4) { output[k] = "X won"; break;}
            else if(o==4) { output[k] = "O won"; break;}

            x=0; o=0;
            for(int i=0; i<4; i++)
                if(input[k][i][l]=='.') break;
                else if(input[k][i][l]=='T') { x++; o++; }
                else if(input[k][i][l]=='X') x++;
                else if(input[k][i][l]=='O') o++;
            if(x==4) { output[k] = "X won"; break;}
            else if(o==4) { output[k] = "O won"; break;}
            if(output[k]=="X won" || output[k]=="O won") continue;

            x=0; o=0;
            for(int i=0; i<4; i++)
                if(input[k][i][i]=='.') break;
                else if(input[k][i][i]=='T') { x++; o++; }
                else if(input[k][i][i]=='X') x++;
                else if(input[k][i][i]=='O') o++;
            if(x==4) { output[k] = "X won"; break;}
            else if(o==4) { output[k] = "O won"; break;}
            if(output[k]=="X won" || output[k]=="O won") continue;

            x=0; o=0;
            for(int i=0; i<4; i++)
                if(input[k][i][3-i]=='.') break;
                else if(input[k][i][3-i]=='T') { x++; o++; }
                else if(input[k][i][3-i]=='X') x++;
                else if(input[k][i][3-i]=='O') o++;
            if(x==4) { output[k] = "X won"; break;}
            else if(o==4) { output[k] = "O won"; break;}
            if(output[k]=="X won" || output[k]=="O won") continue;

            output[k] = "Draw";
            for(int i=0; i<4; i++)
                if(input[k][i][0]=='.' || input[k][i][1]=='.' || input[k][i][2]=='.' || input[k][i][3]=='.') {
                    output[k] = "Game has not completed"; break; }
        }
    }
};
int main() {
    TicTacToeTomek a;
    cout << "Reading input file..." << endl;
    a.readFromFile((char*)"A-large.in");
    cout << "computing solution input file..." << endl;
    a.compute();
    cout << "Writing output file..." << endl;
    a.writeToFile((char*)"A-large.out");
    return 0;
}
