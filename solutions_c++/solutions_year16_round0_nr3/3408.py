#include <iostream> 
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
#include <math.h>
using namespace std;


int send(unsigned long long current, vector < vector <unsigned long long int> > & res){

 bitset <16> vec (current);//cout<<vec.to_string()<<endl;
 vector <unsigned long long> loc (10);
 for(int i=2; i<=10;i++){
	unsigned long long val =0;	
  for(int j=0;j<16;j++){
		if(vec[j]) val += pow(i,j);
	}

	for(unsigned long long int j=2;j<= sqrt(val);j++){
		if(val%j == 0)  {loc[i-1] = j; break;}	
	}
  if(loc[i-1] == 0) return 0;

	if(i==10) loc[0] = val;

 }
	
 res.push_back(loc);	 
 return 1;

}


int main(){

int t;
cin>>t;
int c =1;
int n,j;

while(t--){


cin>>n>>j;
int counter =0;

int i =1;
//bitset <14> vec; 
unsigned long long max =0; 
unsigned long long current =0;


vector < vector <unsigned long long int> > res; 

while(1){

max += pow(2,n-2-i);
current = (1<<i) -1;

while(1){



 unsigned long long real = current*2 +1;
 real += pow(2,n-1);

 int t = send(real,res);	
 if(t == 1) { counter++;}	
 if(counter == j){ goto DONE;}


 if(current == max) break;
 int f = current & -current;
 int r = current + f;		
 current = (((r^current) >> 2) / f) | r; 	

}
i++;


}


DONE: 

cout<<"Case #"<<c<<":"<<endl;
for(int i=0; i< res.size();i++){
	for(int j=0;j<res[i].size();j++){
		if(j ==0) cout<<res[i][j];
		else cout<<" "<<res[i][j];
	}
	cout<<endl; 
}

c++;

}


return 0;
}

 
