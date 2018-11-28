#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream myfile ("B-large.in");
    /*ifstream myfile ("input.in");*/
    ofstream outputfile ("output.txt");
    
    if (myfile.is_open())
    {
        double T_numTests, C_costFactory, F_GainCookiesPerSek, X_Goal;
        myfile >> T_numTests; 
        for (int i = 0; i < T_numTests; i++){
            myfile >> C_costFactory >> F_GainCookiesPerSek >> X_Goal;

            double numFactory = 0.0; 
            double rate = 2.0+F_GainCookiesPerSek*numFactory, bestTime = X_Goal/rate, lastbuilt = 0.0;
                        
            while(lastbuilt<bestTime){
               double timeToGoal = lastbuilt + X_Goal/rate;
               if(timeToGoal < bestTime) bestTime = timeToGoal;
               lastbuilt = lastbuilt + C_costFactory/rate;
               rate = 2.0+F_GainCookiesPerSek*(++numFactory);
                
            }     
            char result[50]; 
            sprintf(result, "%.7f", bestTime);
            outputfile << "Case #" << i+1 << ": " << result << endl; 
            cout << "Case #" << i+1 << ": "; 
            printf("%.7f\n", bestTime);
        }
        myfile.close();
        outputfile.close();
    }
    return 0;
}
