#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>  

using namespace std;

int Deceitful_war(vector<double> blocksN, vector<double> blocksK){
    int winsN_d=0;

    while(blocksN.size() != 0){
        if(blocksN[0]<blocksK[0]){
            blocksN.erase(blocksN.begin());
            blocksK.erase(blocksK.end()-1);
        }
        else{
            blocksN.erase(blocksN.begin());
            blocksK.erase(blocksK.begin());
            winsN_d += 1;
        }
    }

    return winsN_d;
}

int Fair_war(vector<double> blocksN, vector<double> blocksK){
    while(true){
        for(int j = 0; j < blocksK.size(); j++){
            if(blocksN[0]<blocksK[j]){
                blocksN.erase(blocksN.begin());                
            }
        }
        break;
    }
    return blocksN.size();
}

int main(int argc, char* argv[])
{
    ifstream myfile("D-large.in");
    ofstream outputfile ("output.txt");

    if (myfile.is_open())
    {
        int T_numTests, N_numBlocks;

        myfile >> T_numTests; 
        for (int testcase = 0; testcase < T_numTests; testcase++){
            myfile >> N_numBlocks;
            vector<double> blocksN(N_numBlocks), blocksK(N_numBlocks);

            for (int i = 0; i < N_numBlocks; i++){
                myfile >> blocksN[i];
            }
            for (int i = 0; i < N_numBlocks; i++){
                myfile >> blocksK[i];
            }

            sort (blocksN.begin(),blocksN.end());    
            sort (blocksK.begin(),blocksK.end());  
            int winsN_d = Deceitful_war(blocksN, blocksK);
            int winsN_f = Fair_war(blocksN, blocksK);

            outputfile << "Case #" << testcase+1 << ": " << winsN_d << " " << winsN_f << endl; 
            cout << "Case #" << testcase+1 << ": " << winsN_d << " " << winsN_f <<endl; 
        }
        myfile.close();
        outputfile.close();
    }
    return 0;
}
