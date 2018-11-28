/* 
 * File:   A.cpp
 * Author: metin
 *
 * Created on April 12, 2014, 3:28 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<float> us;
set<float>them;
set<float>them2;
/*
 * 
 */
int main(int argc, char** argv) {
    
    int T, N, fair, unfair;
    float temp;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        fair=0;
        unfair=0;
        us.clear();
        them.clear();
        them2.clear();
        cin >> N;
        for(int j=0;j<N; j++)
        {
            cin >> temp;
            us.insert(temp);
        }
        for(int j=0;j<N; j++)
        {
            cin >> temp;
            them.insert(temp);
            them2.insert(temp);
        }

        set<float>::iterator usit=us.begin();
        
        for(int j=0; j<N; j++)
        {
            set<float>::iterator it = upper_bound(them.begin(), them.end(),*usit );
            if(it==them.end())
            {
                fair++;
            }
            else
            {
                them.erase(it);
            }
            usit++;
        }
        
        usit=--us.end();
        set<float>::iterator themit=--them2.end();
        for(int j=0; j<N-1; j++)
        {
        //    cout <<"------ "<< *usit << " " << *themit << endl; 
            if(*usit>*themit)
            {
                unfair++;
                usit--;
                themit--;
            }
            else{
//               set<float>::iterator del=themit;
               themit--;
//               them2.erase(del);
               us.erase(us.begin());
            }
        }
        if(*usit>*themit)
            unfair++;
        
        
    //    cout << unfair << " " << fair << endl;
            
//        if(1)
//            printf("Case #%d: Volunteer cheated!\n", i+1);//cout << "cheated!"<< endl;
//        else if(0)
//            printf("Case #%d: Bad magician!\n", i+1);//cout << "bad magician" << endl;
//        else
            printf("Case #%d: %d %d\n", i+1, unfair, fair );

           
    }

    return 0;
}

