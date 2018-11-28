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

int main(){
READ("C-large-1.in");
WRITE("C-large-1.out");

int t; cin >> t;
int i=1;
while(t--){
double c , f , x , counter , produce=2.0 , temp1=0 , temp2=100000000 , positive=0  , ans=0 , my=0;
cin >> c >> f >> x;
counter=x/produce;

while(1)
{
 positive=c/produce;         // Build a farm
 my+=positive;
 produce+=f;                 // So the production increase
 temp1=(x/produce);          // Count the new time (time taken to reach the goal + time taken to build the farm)
 temp1+=my;

 //cout << temp1 << " " << temp2 << " " << positive << endl;

 if(temp1<temp2)temp2=temp1 , ans+=positive;

 else break;

 //system("pause");
}

if(produce!=2)
ans+=x/(produce-f);

if(counter<ans) {cout << "Case #" << i++ << ": " << fixed << setprecision(7) << counter << endl;continue;}

cout << "Case #" << i++ << ": " << fixed << setprecision(7) << ans << endl;

}

}
