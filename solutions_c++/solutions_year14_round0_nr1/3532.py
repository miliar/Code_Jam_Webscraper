#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    
    int T;
    
    cin >> T;
    
    for(int i = 0 ; i < T; i++)
    {
            cout << "Case #" << i+1 << ": ";
            
            int firstPick;
            int secondPick;
            int chosenCard = -1;
            
            int *dashboard = new int[16];
            int *shuffledDashboard = new int[16];
            
            cin >> firstPick;
            
            for(int j = 0; j < 16; j++) cin >> dashboard[j];
            
            cin >> secondPick;
            
            for(int j = 0; j < 16; j++) cin >> shuffledDashboard[j];
            
            for(int j = 0; j < 16; j++)
            {
                    if(dashboard[(firstPick-1)*4+j%4] == shuffledDashboard[(secondPick-1)*4+j/4])
                    {
                         if(chosenCard == -1) chosenCard = dashboard[(firstPick-1)*4+j%4];
                         else 
                         {
                              chosenCard = -2;
                              break;
                         }                                                       
                    }
            }
            
            if(chosenCard == -1) cout << "Volunteer cheated!" << endl;
            else if(chosenCard == -2) cout <<  "Bad magician!" << endl;
            else cout << chosenCard << endl;
            
            delete[] dashboard;
            delete[] shuffledDashboard;
    }
    
    
}
