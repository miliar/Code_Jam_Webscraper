/*
 * opera.cpp
 *
 *  Created on: 11-Apr-2015
 *      Author: ubuntu
 */
#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<string>
#include<string.h>
#include<sstream>
using namespace std;


int main(){
	int t;
	cin>>t;
	int testcase=1;
	while(testcase!=t+1){
		int smax;
		string chars;
		int *array;
		int friends=0;
		int temp=0;
		cin>>smax;
		cin>>chars;
		array = new int[smax+1];
		for(int i=0;i<(int)chars.length();i++)
			array[i] = chars[i]-'0';

		if (smax==0){
			std::string s;
			std::stringstream out;
			out << testcase;
			s = out.str();
			string str = "Case #"+s+": 0\n";
			cout<<str;
			testcase++;
			continue;
		}
		temp = array[0];

		for(int i=1;i<(int)chars.length();i++){
			if(i>temp){
				if(array[i]!=0){
					int x = i-temp;
					friends += x;
					temp += x;
					temp += array[i];
				}
			}
			else{
				temp += array[i];
			}
		}

		std::string s,news;
		std::stringstream out,newout;
		out << testcase;
		newout << friends;
		s = out.str();
		news = newout.str();
		string str = "Case #"+s+": "+news+"\n";
		cout<<str;
		testcase++;
	}
	return 0;
}

