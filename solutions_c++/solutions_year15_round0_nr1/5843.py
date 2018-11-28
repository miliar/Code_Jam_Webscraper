/*
 * FirstQrFifteen.cpp
 *
 *  Created on: 11 kwi 2015
 *      Author: KAMIL
 */
#include <iostream>
#include <cstdlib>
#include <list>
#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main(){
	int t;
	cin>>t;
	int *n;
	vector<string> x;
	n = new int[t];
	string s;
	for(int i=0;i<t;i++){
		cin>>n[i];
		cin>>s;
		x.push_back(s);
	}

	int smax;
	int friends;
	int index;
	int *answer;
	answer = new int[t];
	for(int i=0;i<t;i++){
		s=x[i];
		smax=n[i];
		friends=0;
		index=0;
		for(int j=0;j<smax+1;j++){
			index+=(s[j]-'0');
			if(index==j){
				friends++;
				index++;
			}
		}
		answer[i]=friends;
	}

	for(int i=0;i<t;i++)
		cout<<"Case #"<<(i+1)<<": "<<answer[i]<<endl;


	//for(int i=0;i<t;i++)
		//cout<<n[i]<<x[i]<<endl;


}



