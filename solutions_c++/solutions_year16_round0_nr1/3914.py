#include <iostream> 
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
using namespace std;


int main(){

int t;
cin>>t;
int c =1;
int n;

while(t--){

cin>>n;
if(n==0){
cout<<"Case #"<<c<<": INSOMNIA"<<endl;
c++; 
continue;
}


int counter =0;
vector <int> vec(10);


long long int start = n;

while(1){
long long int m= start;

while(m >0){
int temp = m%10;
if(vec[temp] == 0) { vec[temp] =1; counter++;}
m=m/10;
}

if(counter == 10) break;
start = start +n;

} 


cout<<"Case #"<<c<<": "<<start<<endl;


c++;

}


return 0;
}

 
