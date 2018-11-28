#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <utility>
#include <functional>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;


ifstream ifs;
ofstream ofs;
string buf;



int main(int argc, char **argv){

    
    ifs.open("D-small-attempt2.in");
    ofs.open("D-small-attempt2.out");
    
	int T = 0;
    ifs >> T;

	rep(i, T){
        ofs << "Case #" << i + 1 << ": ";

        int X, R, C;
        ifs >> X >> R >> C;

        if(X == 1){
            ofs << "GABRIEL" << endl;
        }
        else if(X == 2){
            if(R % 2 == 0 || C % 2 == 0){
                ofs << "GABRIEL" << endl;
            }
            else{
                ofs << "RICHARD" << endl;
            }
        }
        else if(X == 3){
            if(R % 3 != 0 && C % 3 != 0){
                ofs << "RICHARD" << endl;
            }
            else if(R == 1 || C == 1){
                ofs << "RICHARD" << endl;
            }
            else{
                ofs << "GABRIEL" << endl;
            }
        }
        else if(X == 4){
            if(R <= 3 && C <= 3){
                ofs << "RICHARD" << endl;
            }
            else if(R <= 2 || C <= 2){
                ofs << "RICHARD" << endl;
            }
            else{
                ofs << "GABRIEL" << endl;
            }
        }
	}
	

    ifs.close();
    ofs.close();
    return 0;
}
