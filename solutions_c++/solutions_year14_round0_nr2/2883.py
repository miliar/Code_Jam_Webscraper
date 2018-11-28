/* 
 * File:   A.cpp
 * Author: metin
 *
 * Created on April 12, 2014, 3:28 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    int T;
    double C, X, F, R, time;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        R=2;
        time=0;
        cin >> C >> F >> X;
        there:
        
        double lhs= (X-C)/R;
        double rhs= X/(R+F);
        if(lhs>rhs)
        {
            time+=C/R;
           // cout<<C/R << endl;
            
            R+=F;
            
            
            goto there;
        }
        time+=(X/R);
//        if(1)
//            printf("Case #%d: Volunteer cheated!\n", i+1);//cout << "cheated!"<< endl;
//        else if(0)
//            printf("Case #%d: Bad magician!\n", i+1);//cout << "bad magician" << endl;
//        else
            printf("Case #%d: %.7f\n", i+1, time);

           
    }

    return 0;
}

