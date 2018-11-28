#include<iostream>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ofstream fout("ans1.txt");
	ifstream fin("inp1.IN");
	int t;
	fin>>t;
	int tt=0;
	while(tt++!=t){
		int n,total=0;
		fin>>n;
		int sen[n];
		for(int i=0;i<n;++i){
			fin>>sen[i];
			total+=sen[i];
		}
		fout<<"Case #"<<tt<<": ";
		while(total>0){
		int hi=0;
		for(int i=0;i<n;++i)
			if(sen[i]>sen[hi])
				hi=i;
		--sen[hi];		
		fout<<(char)(hi+65);
		total--;
		if(total>0){
			for(int i=0;i<n;++i)
				if(sen[i]>sen[hi])
					hi=i;
			if(sen[hi]>total/2){
				--sen[hi];
				--total;
				fout<<(char)(hi+65);
			}		
		}
		
		fout<<" ";					
		}
		
		
		fout<<"\n";	
//		fout<<"\n\n\n\n\n";	
		
	}

}
