#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <istream>
#include <limits>
#include <ios>
#include <time.h>
#include <math.h>
#include <algorithm>
#include <vector>
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

int n;cin >> n;

vector<double> xn;
vector<double> xk;

vector<bool> xo2;
vector<int> xo;
vector<int> xo3;

for(int i = 0;i<n;++i){double t1 = 0;scanf("%lf",&t1);xn.push_back(t1);}
for(int i = 0;i<n;++i){double t1 = 0;scanf("%lf",&t1);xk.push_back(t1);}



sort(xk.begin(),xk.end());
sort(xn.begin(),xn.end());
int cnt = 0;
int l = 0;int j = 0;int k  =0;
while(l< n || j < n){
++cnt;

if(j==n){xo2.push_back(true);++l;continue;}
if(l==n){xo2.push_back(false);++j;continue;}

if(xn[l] < xk[j]){xo2.push_back(true);++l;continue;}
if(xn[l] > xk[j]){xo2.push_back(false);++j;continue;}



}

xo.push_back(0);int t =0;
for(int i  =0;i<2*n;++i){

if(xo2[i] && xo[t] >= 0){++xo[t];continue;}
if(xo2[i] && xo[t] < 0){xo.push_back(1);++t;continue;}

if(!xo2[i] && xo[t] >=0 ){xo.push_back(-1);++t;continue;}
if(!xo2[i] && xo[t] < 0){--xo[t];continue;}

}


for(int i = 0;i<xo.size();++i){xo3.push_back(xo[i]);}






int ans1 = 0;int ans2 = 0;

for(int i  =0;i<xo.size()-1;++i){


if(xo[i] > 0){

for(int j1  = i;j1 < xo.size();++j1){
if(xo[j1]<0){

xo[j1]+=xo[i];


if(xo[j1]>0){xo[i] = xo[j1];xo[j1]= 0;}
else{xo[i] = 0;}




}
}




}

if(xo[i] < 0 ){

//ans1-=xo[i];


}



}



for(int i  =0;i< xo.size();++i){


if(xo[i] > 0){ans1= ans1+xo[i];

}


}






for(int i  =xo3.size()-1;i>=0;--i){


if(xo3[i] > 0){
ans2+=xo3[i];
for(int j1  = i;j1 >=0;--j1){
if(xo3[j1]<0){

xo3[j1]+=xo3[i];


if(xo3[j1]>0){xo3[i] = xo3[j1];xo3[j1]= 0;}
else{xo3[i] = 0;}




}
}



}

if(xo3[i] < 0 ){


for(int j1  = 0;j1 < i;++j1){
if(xo3[j1]>0){

xo3[j1]+=xo3[i];


if(xo3[j1]<0){xo3[i] = xo3[j1];xo3[j1]= 0;}
else{xo3[i] = 0;}




}
}



//ans1-=xo3[i];


}



}









cout << "Case #"<< b-a+1 << ": " << ans2 << " " << ans1  <<endl;


--a;
}


return 0;

}







