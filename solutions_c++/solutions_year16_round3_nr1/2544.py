#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(int argc, char **argv)
{    
	ifstream infile;
	ofstream ofile;
	ofile.open("output.txt");
	infile.open ("A-large.in");
	int t;infile>>t;
	
	for(int ti=0;ti<t;ti++){
		ofile<<"Case #"<<ti+1<<": ";
		int n;
		infile>>n;
		int a[27];
		int max=0,maxc=0,i1[4],sum=0;
		
		for(int i=0;i<n;i++) {infile>>a[i];sum+=a[i];}
		
		cout<<sum<<endl;
	while(sum> 0){
			
		max=0;
		for(int i=0;i<n;i++){
			if(a[i]>max) max=a[i];
		}	
		cout<<max<<endl;
		 maxc=0;
		for(int i=0;i<n && maxc<2;i++){
			if(a[i]==max) {
				i1[maxc]=i;
				maxc++;
				
			}
		}	
		cout<<maxc<<endl;
		if(sum==3){
			for(int i=0;i<n;i++)
				if(a[i]>0 && i!=i1[0] && i!=i1[1] )
					{ofile<<(char)(i+65)<<" ";a[i]--;}
		}
 
      if(maxc==2){
		  ofile<<(char)(i1[0]+65)<<(char)(i1[1]+65)<<" ";
		  a[i1[0]]--;a[i1[1]]--;
	  }	
		cout<<i1[0]<<endl;
	if(maxc==1 && a[i1[0]] >=2){
		  ofile<<(char)(i1[0]+65)<<(char)(i1[0]+65)<<" ";
		  a[i1[0]]-=2;
	  }	
		sum=0;
		for (int j=0;j<n;j++) sum+=a[j];
		
		cout<<sum<<endl;//*/
		
	}
	ofile<<"\n";
	}
	  
	return 0;
}
