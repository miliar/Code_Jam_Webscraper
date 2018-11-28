#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve()
{
    double cost, farm, target;
    double rate;
    double total;
    double timeTar, timeFar, timeTarFar;
    int cases, current;
    current = 1;
    bool solved;
    cin >> cases;
    for(int x=0;x<cases;x++)
    {
        solved = false;
        total = 0;
        rate = 2.0;
        cin >> cost >> farm >> target;
        while(!solved)
        {
            timeTar = target/rate;
            timeFar = cost/rate;
            timeTarFar = timeFar + (target/(rate+farm));
            //cout << "Data: " << timeTar << " " << timeFar << " " << timeTarFar << endl;     
            if(timeTar < timeTarFar)
            {
                total += timeTar;
                solved = true;
            }
            else
            {
                total += timeFar;
                rate = rate+farm;
            }  
        }
        cout << "Case #" << current << ": " << setprecision(10) << total << endl;
        current++;
    }    
}

int main()
{
    solve();
    return 0;
}
