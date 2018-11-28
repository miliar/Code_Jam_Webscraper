//
//  main.cpp
//  magictrick
//
//  Created by Jun on 14. 4. 12..
//  Copyright (c) 2014년 Albert. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
    ifstream ifs("A-small-attempt6.in");
    ofstream ofs("output");
    int theCase= 0;
    int firstRow =0;
    int secondRow = 0;
    vector<int> first;
    vector<int> second;
    
    vector<int> x;
    vector<int> y;
    vector<int> a;
    vector<int> b;
    vector<int> c;
    vector<int> d;
    int temp = 0;
    ifs>>theCase;
    for (int i= 0; i< theCase; i++){
        ifs>>firstRow;
        if (firstRow == 1){
            for (int h= 0; h<4; h++){
                ifs>>temp;
                a.push_back(temp);
            }
            x=a;
 
            
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            

        }
        
        else if (firstRow == 2){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
                b.push_back(temp);
            }
            x=b;
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
        
        }
        
        else if (firstRow == 3){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
                c.push_back(temp);
            }
            x=c;
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
         
        }
        
        else if (firstRow == 4){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }

            for (int h= 0; h<4; h++){
                ifs>>temp;
                d.push_back(temp);
            }
            x=d;
                        
        }
        
        a.clear();
        b.clear();
        c.clear();
        d.clear();
        
        ifs>>secondRow;

        if (secondRow == 1){
            for (int h= 0; h<4; h++){
                ifs>>temp;
                a.push_back(temp);
            }
            y= a;
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
        }
        
        else if (secondRow== 2){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
                b.push_back(temp);
            }
            y=b;
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
        }
        
        else if (secondRow == 3){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
                c.push_back(temp);
            }
            y=c;
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
        }
        
        else if (secondRow == 4){
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }
            for (int h= 0; h<4; h++){
                ifs>>temp;
            }

            for (int h= 0; h<4; h++){
                ifs>>temp;
                d.push_back(temp);
            }
            y=d;
                    }

        
        int theNum = 0;
        int theCount = 0;
        
        
        for (size_t i= 0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if (x[i] == y[j]){
                    theCount++;
                    theNum = x[i];
                }
                
        }
        }
        cout<<"Case #"<<i+1<<": ";
        ofs<<"Case #"<<i+1<<": ";
        if (theCount == 1){
            
            cout<<theNum<<endl;
            ofs<<theNum<<endl;
        }
        
        else if(theCount == 0){
            cout<<"Volunteer cheated!"<<endl;
            ofs<<"Volunteer cheated!"<<endl;
        }
        
        else{
            cout<<"Bad magician!"<<endl;
            ofs<<"Bad magician!"<<endl;
        }
        
        a.clear();
        b.clear();
        c.clear();
        d.clear();
        

}
}
