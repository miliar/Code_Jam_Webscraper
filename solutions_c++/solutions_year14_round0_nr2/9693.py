#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int cases;
    double goal;
    double cost;
    double extra;
    int farms;
    
    int lastFarms;
    double lastTime;
    double time;
    
    double speed;
    
    ifstream fin("B-small-attempt0.in");
    if (!fin) return 0;
    
    ofstream out("results.txt");
    
    fin >> cases;
    
    for(int i = 1; i <= cases; i++)
    {
       fin >> cost >> extra >> goal;
       lastTime = time = goal / 2;
       lastFarms = farms = 0;
       farms = 0;
       
       do
       {
            // cout << "Case " << i << endl;
             lastTime = time;
             lastFarms = farms;
             time = farms = 0;
           while (farms  <= lastFarms)
           {
                 speed = 2 + extra * farms;
                 time += cost / speed;
                 farms++;
                 //cout << "Bought farm " << farms << endl;
                 //cout << "Current time " << time << endl;
           }
           speed = 2 + extra * farms;
           time += goal / speed;
           //cout << "Final Speed: " << speed << endl;
           //cout << "Farms: " << farms << endl;
           //cout << "Time: " << time << endl;
       } while (time < lastTime);
       
       out << "Case #" << i << ": " << setprecision(7) << fixed << lastTime << endl;
    }
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
