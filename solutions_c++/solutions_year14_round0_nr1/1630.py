//
//  main.cpp
//  Code Jam 1
//
//  Created by Rishab Mehra on 12/04/14.
//  Copyright (c) 2014 Rishab Mehra. All rights reserved.
//

#include <iostream>
#include <fstream>


int a;

using namespace std;
int check(ifstream &fin)
{
    int arr[4][4];
    int arr1[4][4];
    int x,y;
    int count=0;
    fin>>x;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            fin>>arr[i][j];
        }
    }
    
    fin>>y;
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            fin>>arr1[i][j];
        }
    }
    
    for (int i=0; i<4; i++) {
        for (int j=0;j<4;j++)
            if (arr[x-1][i]==arr1[y-1][j]) {
                count++;
                a=arr1[y-1][j];
            }
    }
    
    if (count==0) {
        return 0;
    }
    
    if (count==1) {
        return 1;
    }
    
    return 2;
}

int main() {
    ifstream fin("Test1.txt",ios::in);
    if(fin)
        cout<<"Worked";
    else
        cout<<"Not Worked";
    int x;
    cin>>x;
    
    int arr[100];
    int arr1[100];
    
    for (int i=0; i<x;i++) {
        arr[i]=check(fin);
        arr1[i]=a;
    }
    
    for (int i=0; i<x; i++) {
        cout<<"Case #"<<i+1<<": ";
        if (arr[i]==0) {
            cout<<"Volunteer cheated!";
        }
        
        else if (arr[i]==1) {
            
            cout<<arr1[i];
        }
        
        else
            cout<<"Bad magician!";
        
        cout<<endl;

    }
}

