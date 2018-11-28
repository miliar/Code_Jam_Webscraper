/* 
 * File:   main.cpp
 * Author: Parnami
 * Created on April 12, 2014, 5:26 AM
 * Description : Google Code Jam 2014 Qualification Round. Question 2
 */

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    int t,i,j,l;
    double c,f,x,offset,t1,cookies,step,minner = 999999999999,prev,current;
    ifstream input_data("B-large.in");
    ofstream outputFile("out3.txt");
    FILE *f1;
    f1 = fopen("outterLarge.txt","w+");
    //input_data.open;
    input_data>>t;
    for(l=0;l<t;l++)
    {
        input_data>>c>>f>>x;
        outputFile<<"Question is : "<<c<<" "<<f<<" "<<x<<endl;
        step = f;
        f=2;
        minner = x/f;
        prev = x/f;
        offset = c/f;
        f+=step;
        current = offset+(x/f);
        while(prev>=current)
        {
            offset += c/f;
            f+=step;
            t1 = x/f;
            prev = current;
            current = t1+offset;
            //outputFile<<f;
            //outputFile<<" <- Time taken for this : "<<t1<<" and offset : "<<offset<<endl;
            if(offset+t1<minner)
            {
                minner = t1+offset;
            }
        }
        fprintf(f1,"Case #%d: ",l+1);
        fprintf(f1,"%0.7lf\n",prev);
    }
    return 0;
}

