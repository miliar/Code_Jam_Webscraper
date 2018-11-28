#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>
#include<climits>
#include<math.h>
#include<vector>
#include<stdlib.h>

int t,cc, tot1, tot2, diff, maxDiff;

int main()
{
    ifstream fin("A-large.in");
    //ifstream fin("test.txt");
	ofstream fout("output.txt");

	if(!fin.is_open())
        cout<<"file not loaded"<<endl;

	fin>>t;
	cout<<t<<endl;

	for(int i=1; i<=t; i++)
    {
        tot1=0; tot2=0; maxDiff = 0;
        fin>>cc;
        int* arr=new int[cc];
        fin>>arr[0];
        for(int j=1; j<cc; j++)
        {
            fin>>arr[j];
            diff = arr[j-1]-arr[j];

            if (diff>maxDiff && diff>0)
                maxDiff = diff;

            if(diff>0)
               tot1 +=arr[j-1]-arr[j] ;
        }

        for(int j=0; j<cc-1; j++)
        {
            if(arr[j]>maxDiff)
                tot2 += maxDiff;
            else
                tot2+= arr[j];
        }

        cout<<"Case #"<<i<<": "<<tot1<<" "<<tot2<<endl;
        fout<<"Case #"<<i<<": "<<tot1<<" "<<tot2<<endl;
    }
}
