/** @Image calibration application
 ** @Estimate fundamental or homography matrix
 ** @author Zhe Liu
 **/
/*
Copyright (C) 2011-2013 Zhe Liu.
All rights reserved.

This file is part of the KVLD library and is made available under
the terms of the BSD license (see the COPYING file).
*/
#include<iostream>
#include<vector>
#include <fstream>
#include <string>
using namespace std;

template<typename T>
struct Mat{
	vector<T> data;
	int row, col;

	Mat(int row, int col): row(row),col(col){
		data.resize(row*col);
	}
	Mat(int row, int col, const T& val): row(row),col(col){
		data.resize(row*col,val);
	}

	inline T& operator()(int i, int j){
		return data[i*col+j];
	}

	inline const T& operator()(int i, int j)const {
		return data[i*col+j];
	}

	Mat transpose(){
		Mat out(col, row);
		for(int i=0; i<row;i++)
			for (int j =0;j<col;j++)
				out(j,i)=data[i*col+j];
		return out;
	}
};

//template<typename T>
ofstream& operator<<(ofstream& out,  const Mat<int>& M ){
	for(int i=0; i<M.row;i++){
		for (int j =0;j<M.col;j++){
			out<<M(i,j)<<" ";		
		}
		out<<endl;
	}
	return out;
}


int main() {
	ifstream input("A-small-attempt0.in");
	//ifstream input("A-large.in");
	if(!input.is_open()) {
		cerr<< "problem"<<endl;
	}
	
	int number;
	input>>number;

	vector<int> result(number+1,-1); 

	for(int it=1;it<= number; it++){
		//loading
		int N;
		input >>N;
		vector<string> T;
		for (int i=0; i< N; i++ ) {
			std::string sub;
			input>>sub;
			T.push_back(sub);
		}
	
		//if possible
		vector<vector<char>> es(T.size());
		vector<vector<int>> cards(T.size());
		

		for (int j=0; j< T.size(); j++ ) 
		{
			es[j].push_back(T[j][0]);
			cards[j].push_back(1);
			for (int i=1; i< T[j].size(); i++ ) {
				if (T[j][i]!=T[j][i-1])
				{
					es[j].push_back(T[j][i]);
					cards[j].push_back(1);
				}
				else
				{
					cards[j][cards[j].size()-1]++;
				}
			}
		}

		//for (int i=0; i< es[0].size(); i++ ) {
		//	cout<<cards[0][i]<<" ";
		//}
		cout<<it<<endl; 
		bool posi= true;
		for (int j=1; j< T.size(); j++ ) {

			if (es[0].size()!=es[j].size()) {
				posi=false;
				continue;
			}
			for (int i=0; i<es[0].size(); i++ ) {
				if (es[0][i]!=es[j][i]) posi=false; 
			}
		}

		if(!posi) continue;
		vector<int> st(cards[0].size());
		for (int j=0; j< T.size(); j++ ) {
			for (int i=0; i<cards[j].size(); i++ ){
				st[i]+=cards[j][i];
			}
		}
		for (int i=0; i<cards[0].size(); i++ ){
			st[i]=(st[i]+0.5)/T.size();
		}



		int move=0;
		for (int j2=0; j2< T.size(); j2++ ) {

			for (int i=0; i< cards[j2].size(); i++ ) {
				move+=abs(st[i]-cards[j2][i]);
			}
		}
	
			
		
		result[it]=move;
		
	}
	//output
	ofstream output("answer.txt");
	for(int i=1;i<=number;i++){
		output<<"Case #"<<i<<": ";
		
		if (result[i]<0) output<<"Fegla Won"<<endl;
		else output<<result[i]<<endl;
	}
	output.close();

	return 0;
}

