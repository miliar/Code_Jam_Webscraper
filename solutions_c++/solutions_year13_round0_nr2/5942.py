    #include <iostream>
    #include <fstream>

    using namespace std;

    ifstream fin("in.txt");
    ofstream fout("out.txt");

    int pelouse[100][100];
    int nbLignes, nbCols;

    bool verifCase(int lig, int col)
    {
            int var = pelouse[lig][col];
            bool valide1=true, valide2=true;
            for(int compt = 0; compt<nbLignes; compt++)
            {
                    if(var<pelouse[compt][col])
                    {
                            valide1=false;
                            break;
                    }
            }
            for(int acompt=0; acompt<nbCols; acompt++)
            {
                    if(var < pelouse[lig][acompt])
                    {
                            valide2=false;
                            break;
                    }
            }

            return (valide1 || valide2);
    }

    bool verifPelouse()
    {
            for(int lig=0; lig<nbLignes; lig++)
            {
                    for(int col=0;col<nbCols; col++)
                    {
                            if(!verifCase(lig,col))
                            {
                                    return false;
                            }
                    }
            }
            return true;
    }

    int main(void)
    {
            int nbTests;
            fin >> nbTests;

            for(int test=0; test < nbTests; test++)
            {
                    fin >> nbLignes;
                    fin >> nbCols;

                    for(int i=0; i<nbLignes; i++)
                    {
                            for(int j=0; j<nbCols; j++)
                                    fin >> pelouse[i][j];
                    }

                    if(verifPelouse())
                    {
                            fout << "Case #" << test+1 << ": YES\n";
                    }
                    else
                    {
                            fout << "Case #" << test+1 << ": NO\n";
                    }
            }

            return 0;
    }
