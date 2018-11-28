#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <istream>
#include <limits>
#include <ios>
#include <time.h>
#include <math.h>
using namespace std;

bool isp(int x,int a,int b){

for(int i  =1;i<=a;++i)
{
if(x%i==0 && x/i<=b){return false;}
}
return true;
}



int main(){
int a,b;
cin >> a;
b= a;
while(a>0){


int x,y;int c[4];int d[4];
cin >> x;

for(int i = 0;i<4;++i)
{
int t ;
if(i+1==x){cin >> c[0]>>c[1] >> c[2] >> c[3];}
else{cin >> t>> t>> t>> t;}
}



cin >> y;

for(int i = 0;i<4;++i)
{
int t ;
if(i+1==y){cin >> d[0]>>d[1] >> d[2] >> d[3];}
else{cin >> t>> t>> t>> t;}
}

int ans = 0;int cnt = 0;
for(int i = 0;i<4;++i){
for(int j = 0;j<4;++j){
if(c[i]==d[j]){++cnt;ans = c[i];}
}

}

if(cnt==1){cout << "Case #"<< b-a+1 << ": " << ans <<endl;}
if(cnt>1){cout << "Case #"<< b-a+1 << ": " << "Bad magician!" <<endl;}
if(cnt==0){cout << "Case #"<< b-a+1 << ": " << "Volunteer cheated!" <<endl;}


--a;
}


return 0;

}







