#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    ifstream file("B-large.in");
    ofstream output;
    output.open("output.txt", ios::trunc);

    string iline = "";

    unsigned short heights[100][100];
    string dimensionline;
    string sourceline;
    int dimensions[2];
    bool rowvalid;
    bool columnvalid;
    bool possible;

    int cases;
    getline(file,iline);
    stringstream(iline) >> cases;

    for(int x = 1; x <= cases; x++){
        dimensionline = "";
        getline(file,dimensionline);

        for(int w = 0; w <= 1; w++){dimensions[w] = 0;}

        int currentd = 1, multiply = 1;

        for(int i = dimensionline.length() - 1; i >= 0; i--){
            if(dimensionline[i] == ' '){
                multiply = 1;
                currentd--;
            }
            else{
                dimensions[currentd] += (((int) dimensionline[i] - 48) * multiply);
                multiply *= 10;
            }
        }

        for(int co = 0; co <= 99; co++){for(int ro = 0; ro <= 99; ro++){heights[co][ro] = 0;}}

        for(int row = 0; row <= dimensions[0] - 1; row++){
            sourceline = "";
            getline(file,sourceline);

            int column = dimensions[1] - 1;
            int multiply = 1;

            for(int j = sourceline.length() - 1; j >= 0; j--){
                if(sourceline[j] == ' '){
                    multiply = 1;
                    column--;
                }
                else{
                    heights[column][row] += (((int) sourceline[j] - 48) * multiply);
                    multiply *= 10;
                }
            }
        }

        possible = true;

        if(dimensions[0] == 1 || dimensions[1] == 1){possible == true;}
        else{
            for(int columns = 0; columns <= dimensions[1] - 1; columns++){
                for(int rows = 0; rows <= dimensions[0] - 1; rows++){
                    rowvalid = true;
                    columnvalid = true;
                    for(int tc = 0; tc <= dimensions[1] - 1; tc++){
                        if(heights[tc][rows] > heights[columns][rows]){columnvalid = false;}
                    }
                    for(int tr = 0; tr <= dimensions[0] - 1; tr++){
                        if(heights[columns][tr] > heights[columns][rows]){rowvalid = false;}
                    }
                    if(rowvalid == false && columnvalid == false){possible = false;}
                }
            }
        }

        if(possible == true){output << "Case #" << x << ": YES" << '\n';}
        else{output << "Case #" << x << ": NO" << '\n';}
    }

    file.close();
    output.close();

    return 0;
}
