#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <memory.h>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;


int main(){

	ofstream myfile;
	myfile.open ("/Users/mac/Desktop/out.txt");
    ifstream filein ("/Users/mac/Desktop/A-small-attempt0.in.txt");
    int t,r1,r2;
    int arr1[5][5];
    int arr2[5][5];
    filein >> t;

    for(int T=1;T<=t;T++) {
    	filein >> r1;
    	for(int i=0;i<4;i++)
    		for(int j=0;j<4;j++)
    			filein >> arr1[i][j];

    	filein >> r2;
    	for(int i=0;i<4;i++)
    		for(int j=0;j<4;j++)
    			filein >> arr2[i][j];

    	int occCounter = 0;
    	int no = 0;
    	for(int i=0;i<4;i++)
    		for(int j=0;j<4;j++)
    			if(arr1[r1-1][i] == arr2[r2-1][j]) {
    				occCounter++;
    				no = arr1[r1-1][i];
    			}
    	string ans = "";
    	if(occCounter == 0)
    		ans = "Volunteer cheated!";
    	else if(occCounter > 1)
    		ans = "Bad magician!";

    	if(ans != "")
    		myfile << "Case #" << T << ": " << ans << endl;
    	else
    		myfile << "Case #" << T << ": " << no << endl;
    }
 
	  myfile.close();

}