#include<iostream>
#include<vector>
#include<sstream>
#include<fstream>
#include<climits>

using namespace std;


int main()
{
	ifstream fin("lawn.in");
	ofstream fout("lawn.out");
	int testcases;
	int n,m;
	fin>>testcases;
	int count=1;
	while(testcases--){
		fin>>n>>m;
		vector<vector<int> > mat(n);
		vector<vector<int> >::iterator itr;
		for(itr=mat.begin();itr<mat.end();itr++){
			itr->resize(m);
		}
		vector<int>::iterator itrc;
		for(itr=mat.begin();itr<mat.end();itr++){
			for(itrc=itr->begin();itrc<itr->end();itrc++)
				fin>>*itrc;
		}
		/*
		for(itr=mat.begin();itr<mat.end();itr++){
		  for(itrc=itr->begin();itrc<itr->end();itrc++)
		  cout<<*itrc;
		  cout<<endl;
		  }
		  getchar();*/
		bool isdone=false;
		while(!isdone){
			int min=INT_MAX;
			vector<vector<int> >::iterator ritr; 
			int cpos;
			int j;

			for(itr=mat.begin();itr<mat.end();itr++){
				for(itrc=itr->begin(),j=0;itrc<itr->end();itrc++,j++){
					if(*itrc<min){
						min=*itrc;
						ritr=itr;
						cpos=j;
					}
				}
			}		
			bool isRowValid=true;
			bool isColValid=true;

			for(itrc=ritr->begin();itrc<ritr->end();itrc++){
				if(*itrc > min){
					isRowValid=false;
					break;
				}
			}
			for(itr=mat.begin();itr<mat.end();itr++){
				if((*itr)[cpos]>min){
					isColValid=false;
					break;
				}
			}
			if(!isRowValid && !isColValid){
				fout<<"Case #"<<count<<": NO"<<endl;
				isdone=true;
			}
			else{
				if(isRowValid){
						mat.erase(ritr);
					if(mat.size()==0){
						fout<<"Case #"<<count<<": YES"<<endl;
						isdone=true;
					}
				}
				if(!isdone && isColValid){
					for(itr=mat.begin();itr<mat.end();itr++){
						itr->erase(itr->begin()+cpos);
					}
					
					if(mat.begin()->size()==0){
						fout<<"Case #"<<count<<": YES"<<endl;
						isdone=true;
					}
				}

			}
	/*	
			for(itr=mat.begin();itr<mat.end();itr++){
		  		for(itrc=itr->begin();itrc<itr->end();itrc++)
		  			cout<<*itrc;
		  		cout<<endl;
		  	}
			getchar();*/
		}

		count=count+1;
		/*for(itr=mat.begin();itr<mat.end();itr++){
			itr->clear();
		}
		mat.clear();*/
	}


	return 0;
}
