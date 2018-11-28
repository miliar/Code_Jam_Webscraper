#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(){

    ifstream in("A-small-attempt0.in");
    ofstream out("output.txt");

    int n=0, r1=0, r2=0, p=0, m=1;
    int fQuestion[4], sQuestion[4];

    in >> n;

    while(n--){

        in >> r1;

        for(int i=0; i<4; i++){

            if(i+1 == r1){
                for(int j=0; j<4; j++){
                        in >> fQuestion[j];
                }
            }
            else{
                for(int j=0; j<4; j++){
                        in >> p;
                }
            }
        }

        in >> r2;

        for(int i=0; i<4; i++){

            if(i+1 == r2){
                for(int j=0; j<4; j++){
                        in >> sQuestion[j];
                }
            }
            else{
                for(int j=0; j<4; j++){
                        in >> p;
                }
            }
        }

        p=0;

        for(int i =0; i<4; i++){
            for(int j=0; j<4; j++){
                if(fQuestion[i] == sQuestion[j]){
                    p++;
                    r1 = fQuestion[i];
                }
            }
        }

        if(p==0)
            out << "Case #" << m << ": " << "Volunteer cheated!";
        else if(p == 1)
            out << "Case #" << m << ": " << r1;
        else if(p > 1)
            out << "Case #" << m << ": " << "Bad magician!";

            out << "\n";
            m++;

    }

        in.close();
        out.close();

    return 0;
}
