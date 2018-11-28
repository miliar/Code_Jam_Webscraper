//
//  main.cpp
//  codejam
//
//  Created by Fahad Mansoor on 12/04/2014.
//  Copyright (c) 2014 pirilano. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#define debug 0
using namespace std;
vector<vector<int> > readVector(int size_X,int size_Y)
{
    vector<vector<int> > V = vector<vector<int>>();
    for (int i=0; i < 4; i++) {
        V.push_back(vector<int>());
        for (int j=0; j < 4; j++) {
            int val=0;
            cin>>val;
            V[i].push_back(val);
            
        }
        //     cout<<endl;
        
    }
    return V;
}
void cookieclicker(int T,double c , double f , double x)
{
    double currentProductionSpeed = 2;
    double oldTimeCost=0;
    while (true) {
        if ( x /(currentProductionSpeed) < (x/(currentProductionSpeed + f) + c/currentProductionSpeed))
        {
            double answer =  oldTimeCost + (x/currentProductionSpeed);
            int digits = log10(roundtol( answer))+1;
            
            cout << "Case #"<<T<<": "<<std::setprecision(digits+ 7)<<answer<<endl;
            break;
        }
        else
        {
            oldTimeCost += c/currentProductionSpeed;
            currentProductionSpeed += f;
        }
    }
}
void StupidMagician(int T)
{
    //    cout<<"\nInput ends"<<endl;
    int firstNo = 0 ;
    int secondNo =0 ;
    cin>>firstNo;
    vector<vector<int>> FirstVector = readVector(4, 4);
    cin>>secondNo;
    vector<vector<int>> SecondVector = readVector(4, 4);
    int matches=0;
    int matchFound=-1;
    for (int i=0; i <4; i++) {
        int toFind =SecondVector[secondNo-1][i];
        if (find(FirstVector[firstNo-1].begin(), FirstVector[firstNo-1].end(), toFind) != FirstVector[firstNo-1].end())
        {
            matchFound = toFind;
            matches ++;
        }
    }
    
    if ( matches == 1)
    {
        cout << "Case #"<<T<<": "<<matchFound<<endl;
    }
    else if (matches > 1)
    {
        cout << "Case #"<<T<<": "<<"Bad magician!"<<endl;
    }
    else if (matches ==0 )
    {
        cout << "Case #"<<T<<": "<<"Volunteer cheated!"<<endl;
    }
}

int main(int argc, const char * argv[])
{
    int T;
    // freopen("input.txt", "r+", stdin);
    cin>>T;
    int i =0;
    while (i< T) {
        double x=0,c=0,f=0;
        cin>>c;
        cin>>f;
        cin>>x;
        cookieclicker(i+1, c, f, x);
        i++;
    }
    return 0;
}

