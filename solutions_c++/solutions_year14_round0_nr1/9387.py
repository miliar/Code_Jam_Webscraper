/**************************
Author : Druid
Date   : 1-4-2014
Problem: Simulation Assignment#2
**************************/

#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <cstring>
#include <string>
#include <numeric>
#include <sstream>
#include <climits>
#include <stack>
#include <stdio.h>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <iomanip>
#include <stdlib.h>

using namespace std;
#define SZ(x)  (int)x.size()
#define PI 3.14159265359

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int arr[4][4];
int main(){
READ("C-large-1.in");
WRITE("C-large-1.out");

int t , i=1; ; cin >> t;
while(t--){
int n ; cin >> n;
map<int,int>mymap;
for(int i=0 ; i<4 ; i++)
for(int j=0 ; j<4 ; j++){
cin >> arr[i][j];
if(n==i+1)mymap[arr[i][j]]++;
}

int counter=0 , temp =0;
cin >> n;

for(int i=0 ; i<4 ; i++)
for(int j=0 ; j<4 ; j++){
cin >> arr[i][j];
if(n==i+1){
if(mymap[arr[i][j]])counter++ , temp=arr[i][j];
}

}

if(counter==0)cout << "Case #" << i++ << ": Volunteer cheated!" << endl;
if(counter==1)cout << "Case #" << i++ << ": " << temp << endl;
if(counter>=2)cout << "Case #" << i++ << ": " << "Bad magician!"  << endl;
}

}
