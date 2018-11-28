#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

    ifstream myFile("input.txt");
    ofstream output("output.txt");
    int t,x,r,c;
    string line;

    string a;
    bool richard = false;

    if(myFile.is_open())
    {
        myFile >> t;
        for(int i = 0; i < t ; i++){
            myFile >> x >> r >> c;
            richard = false;
            if((r*c) % x == 0){
                if(x == 3 && (r < 2 || c < 2))
                        richard = true;
                 else if(x == 4 && (r < 3 || c < 3))
                        richard = true;
                 else if(x == 5 && (r < 4 || c < 4))
                        richard = true;
                 else if(x == 6 && (r < 5 || c < 5))
                        richard = true;

                else if(x >= 7)
                        richard = true;
            }
            else
                richard = true;




                    if(richard)
                        a = "RICHARD";
                    else
                        a = "GABRIEL";
                output << "Case #" << i+1 << ": " << a << "\n";





        }
        output.close();
       myFile.close();

    }
    myFile.close();
}
