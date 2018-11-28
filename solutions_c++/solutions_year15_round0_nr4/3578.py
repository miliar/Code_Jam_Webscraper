#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

void Ominous(const char* filename, const char* filename2){
    std::ifstream infile(filename);
    std::ofstream outfile(filename2);

    std::string line;
    int cases=0;
    std::getline(infile, line);
    std::istringstream iss(line);
    iss >> cases;
    stringstream output;
    for (int tcase=1;tcase<=cases;tcase++){
        std::getline(infile, line);
        int X,R,C;
        std::istringstream iss(line);
        iss>>X>>R>>C;
        if (X==1){
            output<<"Case #"<<tcase<<": GABRIEL"<<endl;
            continue;
        }
        bool choice=false;
        if (R*C%X!=0){
            output<<"Case #"<<tcase<<": RICHARD"<<endl;
            continue;
        }
        if (X==2){
            //the area must be divisble by X
            if (R*C%X==0)
                choice=false;
            else
                choice=true;
        }else{
            if (X==3){
                if (R==1 || C==1){
                    choice=true;
                }else{
                    if (R*C%X==0)
                        choice=false;
                    else
                        choice=true;
                }
            }else{
                //X=4
                if (R<3 || C<3)
                    choice=true;
                else
                    choice=false;
            }
        }

        if (!choice)
            output<<"Case #"<<tcase<<": GABRIEL"<<endl;
        else
            output<<"Case #"<<tcase<<": RICHARD"<<endl;
    }
    outfile << output.str();
    outfile.close();
    infile.close();
}


int main(int argc, char *argv[])
{
    Ominous(argv[1],argv[2]);
    return 0;
}
