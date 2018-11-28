#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream fin;
    ofstream fout;

    int t, first, second, fArran[4][4], sArran[4][4];
    int i, j, k;
    int result, n;

    fin.open("A-small-attempt0.in");
    fout.open("A-small-attempt0.out");

    fin>>t;
    for (i = 0; i < t; i++){
        n = 0;
        fin>>first;

        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){
                fin>>fArran[j][k];

            }
        }


        fin>>second;

        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){
                fin>>sArran[j][k];

            }
        }


        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){


                if (fArran[first-1][j] == sArran[second-1][k]){

                    result = fArran[first-1][j];
                    n++;
                }
            }
        }
        fout<<"Case #"<<i+1<<": ";
        if (n == 0)
            fout<<"Volunteer cheated!"<<endl;
        else if (n == 1)
            fout<<result<<endl;
        else
            fout<<"Bad magician!"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
