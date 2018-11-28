/* 
 * File:   main.cpp
 * Author: devu
 *
 * Created on April 13, 2013, 11:24 AM
 */

#include <cstdlib>
#include<list>
#include<iostream>

using namespace std;

/*
 * 
 */
int arr[100][100];

int maxRight[100];
int maxDown[100];

void checkLawn(int iter) {
    int x, y;
    scanf("%d%d", &x, &y);
    for (int i = 0; i < x; i++) {
        maxRight[i] = -1;
        for (int j = 0; j < y; j++) {
            scanf("%d", &arr[i][j]);
            if (arr[i][j] > maxRight[i])
                maxRight[i] = arr[i][j];
        }
    }
    for (int i = 0; i < y; i++) {
        maxDown[i]=-1;
        for (int j = 0; j < x; j++) {
             if(arr[j][i]>maxDown[i]){
                 maxDown[i]=arr[j][i];
             }           
        }
    }
    //    int prev;
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            if (arr[i][j] < maxRight[i]) {
                if(arr[i][j]<maxDown[j]){
                    cout<<"Case #"<<iter<<": NO"<<endl;
                    return ;
                }
            }
        }
    }
cout<<"Case #"<<iter<<": YES"<<endl;
}

int main(int argc, char** argv) {
    int iter;
    iter = 0;
    int maxiter;
    scanf("%d", &maxiter);
    while (iter < maxiter) {
        iter++;
        checkLawn(iter);
    }

    return 0;
}

