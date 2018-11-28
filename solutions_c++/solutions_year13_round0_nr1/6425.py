#include <iostream>
#include <string>
#include <fstream>
using namespace std;


/*
   X = 88
   O = 79
   T = 84
   OOOO = 316
   OOOT = 321
   XXXX= 352
   XXXT =348
*/


int main()
{
    ifstream myReadFile;
    myReadFile.open("A-large.in");
    ofstream of;
    of.open("A-large.out");
    int t;
    myReadFile >> t;
    cout << t<< endl;
    int n = 1;
    while(t--){
        string  str [4] ;
        for(int i = 0 ; i < 4 ;i++){
                myReadFile >>str[i];
        }
        bool gameon = true;
        bool xw = false;
        bool ow = false;
        
        for(int i =0;i<4;i++)
        {
                int sumr = str[i][0] + str[i][1] + str[i][2] + str[i][3];
                int sumc = str[0][i] + str[1][i] + str[2][i] + str[3][i];
                if(sumr == 316 || sumr == 321 || sumc ==316 || sumc == 321){
                    ow = true;
                    break;
                }
                else if(sumr == 352 || sumr == 348 || sumc == 352 || sumc == 348){
                     xw = true;
                     break;
                }
    
        }
        if(!ow&&!xw){
                int d1 = str[0][0] + str[1][1] + str[2][2] + str[3][3];
                int d2 = str[0][3] + str[1][2] + str[2][1] + str[3][0];
                if( d1 == 316 || d1 == 321 ||d2 == 316 || d2 == 321){
                    ow = true;
                }
                if(d1 == 352 || d1 == 348 || d2 == 352 || d2 == 348){
                    xw = true;
                }
        }
        if(!ow&&!xw){
                     int isdotabsent = 0;
                     for(int i=0;i<4;i++){
                             if(str[i].find('.') == std::string::npos)
                             {
                                 isdotabsent++;
                             }
                     }
                     if(isdotabsent ==4) gameon = false; 
        }
        if(ow)   of << "Case #"<<n<<": O won" <<endl;
        else if(xw)   of << "Case #"<<n<<": X won" <<endl;
        else
        {
            if(gameon) of << "Case #"<<n<<": Game has not completed" <<endl;
            else     of << "Case #"<<n<<": Draw" <<endl;
        }
        n++;
    }
    myReadFile.close();
    of.close();
    return 0;
}
