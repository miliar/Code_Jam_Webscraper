//
//  main.cpp
//  Code Jam 4
//
//  Created by Rishab Mehra on 12/04/14.
//  Copyright (c) 2014 Rishab Mehra. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include<fstream>

using namespace std;

int check(int x,double arr1[],double arr2[]);
int check1(int x,double arr1[],double arr2[]);

int main() {
   
    ifstream fin("Test1.txt");
    int x;
    fin>>x;
    int arr[50],arrr[50];
    double arr1[1000],arr2[1000], arrr1[1000],arrr2[1000];
    int a;
   // int z;
    
    for (int i=0; i<x; i++) {
        fin>>a;
        for (int i=0; i<a; i++) {
            fin>>arr1[i];
            arrr1[i]=arr1[i];
        }
        
        for (int i=0; i<a; i++) {
            fin>>arr2[i];
            arrr2[i]=arr2[i];
        }
        
        //int b=i;
        //int c=a;
        
        arr[i]=check(a,arr1,arr2);
        arrr[i]=check1(a,arrr1,arrr2);
       // if(i==0)
         //   z=arrr[0];
    }
    
    //arrr[0]=z;
    

    for (int i=0; i<x; i++) {
        cout<<"Case #"<<i+1<<": "<<arr[i]<<" "<<arrr[i]<<endl;
    }
    
    return 0;
}
int check(int x,double arr1[],double arr2[])
{
    int count=0;
    
    
    sort(arr1, arr1+x);
    sort(arr2, arr2+x);
    //reverse(arr2, arr2+x);
    for (int i=0;i<x;i++) {
        //cout<<arr1[i]<<" ";
    }
    //cout<<endl;
    int i;
    int size=x;
    for (i=0; i<size; i++) {
      //  cout<<endl<<arr1[0]<<endl;
        if (arr1[0]<arr2[0]) {
            //cout<<arr1[0]<<" "<<arr2[0];
            for (int j=0; j<x-1; j++) {
                int temp=arr1[j];
                arr1[j]=arr1[j+1];
                arr1[j+1]=temp;
            }
            
            
        }
        else {
            for (int j=0; j<x-1; j++) {
                int temp=arr1[j];
                arr1[j]=arr1[j+1];
                arr1[j+1]=temp;
                
                temp=arr2[j];
                arr2[j]=arr2[j+1];
                arr2[j+1]=temp;
                
               // cout<<arr1[0]<<endl;
                
            }
            count++;
        }
        x--;
    }
    
    return count;
    
    
    
    return 0;
}

int check1(int x,double arr1[],double arr2[]) {
    
    sort(arr1, arr1+x);
    sort(arr2, arr2+x);
    
    int checker=0;
    
    int size=x;
    for(int i=0; i<size&&checker==0;i++) {
        checker=1;
        for(int j=0;j<x;j++) {
        if((arr2[j]-arr1[0])>0)
        {
            checker=0;
            for (int k=0; k<x-1; k++) {
                int temp=arr1[k];
                arr1[k]=arr1[k+1];
                arr1[k+1]=temp;
            }
            
            for (int k=j; k<x-1; k++) {
                int temp=arr2[k];
                arr2[k]=arr2[k+1];
                arr2[k+1]=temp;
            }
            x--;
            break;
        }
            
      }
    }
    int a=x;
   // cout<<x;
    return a;
 
}

