//
//  main.cpp
//  Google_Code_Jam
//
//  Created by Jooyeon Lee on 4/12/14.
//  Copyright (c) 2014 Jooyeon Lee. All rights reserved.
//



#include <iostream>
#include <cstdio>

using namespace std;

int main(void){
    cout.precision(10);
    
    double T, C, F, X; //[T: test case], [C: BUY a cookie farm], [F: extra cookie rate], [X: Winner!];
    int caseNum = 0;
    
    cin >> T;
    
    while(T--){
        
        
       // double myCookies = 0;
        double getCookies = 2.0;
       // double cookieTime = 0;
        double cookieTimeWOFarm = 0;
        double cookieTimeWFarm = 0;
        
        cin >> C >> F >> X;
        
        
        //Cookie Time without Farm
        cookieTimeWOFarm = X / getCookies;
        //Cookie Time with Farm
        cookieTimeWFarm = C/getCookies + X/(getCookies+F);
        
        while (cookieTimeWFarm < cookieTimeWOFarm)
        {
            getCookies += F;
            //Cookie Time without Farm
            cookieTimeWOFarm = cookieTimeWFarm;
//           cookieTimeWOFarm = X / getCookies;
            //Cookie Time with Farm
            cookieTimeWFarm = cookieTimeWOFarm - X / getCookies + C / getCookies + X / (getCookies + F);
            
        }
        
        caseNum++;
        cout << "Case #" << caseNum << ": ";
        cout << cookieTimeWOFarm<< endl;
    }
    
    return 0;
}


/*
 
 
 
#include <iostream>
#include <cstdio>

using namespace std;

int main(void){
    int T, A1, A2, AFinal = 0; // T: test case, A: the row of the answer
    int cardArr1[4][4];
    int cardArr2[4][4];
    int caseNum = 0; 
    cin >> T;
    
    while(T--){
        
        cin >> A1;
        for (int i=0; i <4; i++) {
            for (int j= 0; j<4; j++) {
                cin >> cardArr1[i][j];
            }
        }

        cin >> A2;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> cardArr2[i][j];
            }
        }
        
        
        int flag = 0;
        for (int i = 0; i<4; i++) {
            for(int j=0; j < 4; j++){
                if( cardArr1[A1-1][i] == cardArr2[A2-1][j])
                {
                    AFinal = cardArr1[A1-1][i];
                    flag++;
                }
            }
        }
        caseNum++;
        cout << "Case #" << caseNum << ": ";
        if (flag == 0) cout << "Volunteer cheated!" <<endl;
        else if (flag == 1) cout << AFinal << endl;
        else cout << "Bad magician!" << endl;
        

    }
}



*/