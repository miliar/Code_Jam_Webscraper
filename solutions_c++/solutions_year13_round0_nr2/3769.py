#include <fstream>
#include <iostream>

int main(int argc, char *argv[])
{
    //Lawnmower
    std::cout << "Starting solution of problem B..." << std::endl;

    //file names for input and output
    std::string filenameIn = "B-large.in";
    std::string filenameOut = "B-large.out";
    //std::string filenameIn = "B-small-practice.in";
    //std::string filenameOut = "B-small-practice.out";
    //std::string filenameIn = "B-small-attempt1.in";
    //std::string filenameOut = "B-small-attempt1.out";

    std::ofstream os(filenameOut.c_str());

    std::ifstream is(filenameIn.c_str());
    if (is.is_open()){
        int numTestCases = 0;
        is >> numTestCases;

        for (int nCase = 1; nCase <= numTestCases; nCase++){
            std::cout << "Processing case #" << nCase << std::endl;

            //read size of the lawn
            int n = 0;
            int m = 0;
            is >> n >> m;

            int lawn[n][m];
            bool lawnValid[n][m];

            for (int row = 0; row < n; row++){
                for (int col = 0; col < m; col++){
                    int height = 0;
                    is >> height;
                    lawn[row][col] = height;
                    lawnValid[row][col] = false;
                }
            }

            //output lawn
            for (int row = 0; row < n; row++){
                for (int col = 0; col < m; col++){
                    std::cout << lawn[row][col] << " ";
                }
                std::cout << std::endl;
            }

            //each pixel must be in a row or a column with equal heights for all elements

            //iterate through all elements
            for (int y = 0; y < n; y++){
                for (int x = 0; x < m; x++){
                    int height = lawn[y][x];

                    //check if whole column has the same height
                    bool possibleForCol = true;
                    for (int row = 0; row < n; row++){
                        if (height < lawn[row][x]){
                            possibleForCol = false;
                            break;
                        }
                    }
                    if (possibleForCol){
                        lawnValid[y][x] = true;
                        continue;
                    }


                    //check if whole row has the same height
                    bool possibleForRow = true;
                    for (int col = 0; col < m; col++){
                        if (height < lawn[y][col]){
                            possibleForRow = false;
                            break;
                        }
                    }
                    if (possibleForRow){
                        lawnValid[y][x] = true;
                        continue;
                    }
                }
            }

            //check if all lawn elements are valid
            std::string result = "YES";
            for (int row = 0; row < n; row++){
                for (int col = 0; col < m; col++){
                    if (!lawnValid[row][col]){
                        result = "NO";
                        break;
                    }
                }
                if (result == "NO"){
                    break;
                }
            }

            //write result for test case into file
            os << "Case #" << nCase << ": " << result << std::endl;
            std::cout << "Case #" << nCase << ": " << result << std::endl;
        }

    }
    is.close();

    os.close();

    return 0;
}
