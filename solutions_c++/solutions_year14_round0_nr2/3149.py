#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;


int main(int argc, char *argv[])
{
    ifstream fcin("C:\\Users\\zdb\\Downloads\\B-large.in");
    //ifstream fcin("file.txt");
    ofstream fcout("ans1.txt");
    int T; fcin >> T;
    for(int i = 1; i <= T; i++){
         double C = 0;
         double f = 0;
         double X = 0;
         fcin >> C >> f >> X;
         int k = int((X*f-2*C)/(C*f))-1;
         double cost = 0;
         for(int j = 0; j <= k; j++){
                 cost += C/(2+j*f);        
         }
         cost += X/(2+(k+1)*f);
         
         double di = X/2;
         if(cost > di) cost = di;
         fcout << "Case #" << i << ": ";   
         fcout << fixed << setprecision(8) << cost << endl; 
    }    
    system("PAUSE");
    return EXIT_SUCCESS;
}
