#include<iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <limits.h>

using namespace::std;

//=INT_MAX;
ofstream oFile("output.text");
struct Data{

};

int findMin(vector<int> p)
{
	int max=0, index=0, temp1=0, temp2=0;
	vector<int> q;
	//for(int i=0; i<p.size(); i++) oFile<<p[i];
	
	//oFile<<endl;
	for(int i=0; i<p.size(); i++){
		if(max<p[i]){
			max = p[i];	
			index=i;
		}
		if(p[i] <=1 );		
		else 
			q.push_back(p[i]-1);
	}
	if(max<=3) return max;
	temp1 = p[index];
	if(0 == temp1%2){
		p[index]=temp1/2;
		p.push_back(temp1 - temp1/2);
	}	
	else if(0 == temp1%3){
		p[index]=temp1/3;
		p.push_back(temp1 - temp1/3);
	}	
	else{
		p[index]=temp1/2;
		p.push_back(temp1 - temp1/2);
	}
	temp1 = findMin(p)+1;
	temp2 = findMin(q)+1;
	temp1 = temp2 < temp1 ? temp2 : temp1;
	//oFile<<"temp1 "<<temp1<<endl;
	//oFile<<"temp2 "<<temp2<<endl;
	//oFile<<"max "<<max<<endl;
	return(max < temp1 ? max : temp1);	
}
//ofstream oFile("output.text");
int main()
{
	int data=0, d=0, testcases=0;
	
	ifstream iFile("B-small-attempt1.in");//("input.in");//
	vector<int> p;
	int minTime;
	
	if(iFile.is_open()){
		iFile>>testcases;
		//oFile<<testcases<<endl;
		for(int i=1; i<=testcases; i++){
			oFile<<"Case #"<<i<<": ";
			iFile>>d;
			//oFile<<d<<"--";
			for(int i=0; i<d; i++){
				iFile>>data;
				p.push_back(data);
			}
			
			//
			minTime=findMin(p);
			
			p.clear();
			//oFile<<endl;
			oFile<<minTime<<endl;
		}
		iFile.close();
	}
	else
		oFile<<"Can't open input file"<<endl;
	return 0;
}