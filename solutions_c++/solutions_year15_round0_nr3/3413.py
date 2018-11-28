#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
#include<unordered_map>
using namespace std;

int mult[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int prod(int a,int b){
	if(a>0){
		return mult[abs(a)][b];
	}
	else{
		return -(mult[abs(a)][b]);
	}
}


int main(){
	unordered_map<char, int> m;
  m['1']=1; m['i']=2; m['j']=3; m['k']=4;
	
    int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	int t;   file>>t;
	

	int l; int x; string str; 
	for(int x1=1;x1<=t;x1++){
	    file2<<"Case #"<<inc++<<": ";
	    
	
	    file>>l>>x;  file>>str;
	    int ar[l*x+2];
	    ar[0]=1;
	    for(int i=0;i<x;i++){
	    	for(int j=0;j<l;j++){
	    		ar[l*i+j+1]=m[str[j]];	// cout<<ar[l*i+j+1]<<" ";
	    	}
	    }
	    int ans=0;
	    int k1=0,k2=0;
	    for(int i=1;i<=x*l;i++){
	    	ar[i]=prod(ar[i-1],ar[i]); //cout<<ar[i]<<" ";
	    	if(ar[i]==2){
	    		k1=1;
	    	}
	    	if(k1==1&& ar[i]==4){
	    		k2=1;
	    	}
	    }
	    
	    if(k1==1&&k2==1&&ar[x*l]==-1)
	    ans=1;
	    
	    
		if(ans==0) 
		file2<<"NO";
		else
		file2<<"YES";
		
		file2<<endl;
	}
}
