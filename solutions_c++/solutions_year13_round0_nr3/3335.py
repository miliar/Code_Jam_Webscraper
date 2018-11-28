#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

//bool palindromas(int k);
//int laipsnis(int i);

int main()
{
    //cout << "Labas";
    //system("PAUSE");
    //return EXIT_SUCCESS;
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
    int n;
    fin >> n;
    for(int a = 0; a < n; a++){
            int x;
            int y;
            int ats = 0;
            fin >> x >> y;
            
            for(int i = x; i <= y; i++){
                     
                    if(i == 1){
                         ats++;     
                    }else if(i == 9){
                         ats++;     
                    }else if(i == 4){
                         ats++;     
                    }else if(i == 121){
                         ats++;     
                    }else if(i == 484){
                         ats++;     
                    }     
            }
            fout << "Case #" << a+1 << ": " << ats << endl;
    }
}