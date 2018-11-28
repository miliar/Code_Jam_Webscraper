#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) 
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    
    int t;
    double c, f, x;
    
    in >> t;
    
    for (int i = 0; i < t; i++) 
    {
        long double rate = 2;
        long double time = 0;
        long double sTime = 0, fTime2 = 0;
        
        in >> c >> f >> x;
        
        //simulate solution
        
        long double initial = -1;
        while(true)
        {            
            fTime2 = x/(rate);
            sTime = c/rate;
            
            if(initial == -1)
            {
                if(sTime > fTime2)
                {
                    time = fTime2;
                    break;
                }
            }
            else
            {
                if(initial < (time+fTime2) && (initial != -1))
                {
                    time = initial;
                    break;
                }
            }            
            if(initial == -1)
                initial = fTime2;
            else
                initial = time+fTime2;
            rate += f;
            time += sTime;
        }
        
        out.setf(ios::fixed, ios::floatfield);
        out.precision(7);
        out << "Case #" <<i+1 << ": " << time << endl;
    }

    in.close();
    out.clear();

    return 0;
}

