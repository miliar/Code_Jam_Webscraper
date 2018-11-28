/*
 * main.cpp
 *
 *  Created on: 2013.04.13.
 *      Author: Peti
 */

#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;



int main(){
	int t; //test cases
	int i,j,k;
	int sor,oszlop,sora,oszlopa;
	bool lehetseges;
	fstream in("B-large.in");
	fstream out("output.txt");
	in>>t;
	for(k=0;k<t;k++){
		in>>sor;
		in>>oszlop;
		lehetseges=true;
		int tomb[sor*oszlop];
		for(i=0;i<sor*oszlop;i++){
			in>>tomb[i];
		}
		/*for(i=0;i<sor;i++){
			for(j=0;j<oszlop;j++){
				cout<<tomb[(i*oszlop)+j]<<" ";
			}
			cout<<"\n";
		}*/
		//---------------------------------------------------------
		for(i=0;i<sor*oszlop;i++){
			oszlopa=i%oszlop;
			sora=i/oszlop;
			bool lehetsegesoszlop=true;
			for(j=0;j<sor;j++){
				if(tomb[i]<tomb[(j*oszlop)+oszlopa]){lehetsegesoszlop=false;}
			}

			bool lehetsegessor=true;
			for(j=0;j<oszlop;j++){
				if(tomb[i]<tomb[(sora*oszlop)+j]){lehetsegessor=false;}
			}
			if(!(lehetsegessor || lehetsegesoszlop)){lehetseges=false;}
			//cout<<lehetseges<<"\n";
		}
		//---------------------------------------------------------
		if(lehetseges){
			cout<<"Case #"<<k+1<<": YES\n";
			out<<"Case #"<<k+1<<": YES\n";
		}else{
			cout<<"Case #"<<k+1<<": NO\n";
			out<<"Case #"<<k+1<<": NO\n";
		}

	}


	return 0;
}








