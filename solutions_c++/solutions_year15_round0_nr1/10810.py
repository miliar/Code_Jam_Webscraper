/*
 * StandingOvation.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Divya
 */

#include<iostream>

int atoi(char c){
    return  c - 48;
}

using namespace std;
int main(){

	int T,maxshyness;
	char shyness[1000];
    
	cin >> T;
	
	for(int i=1; i<=T; ++i){
            int to_invite=0, audi=0;
            cin >> maxshyness;
            cin >> shyness;
            audi = atoi(shyness[0]);
            //cout << " Case #" << i << endl;
            //cout << "initial audiance "<< audi << endl;
            for( int j=1; j<= maxshyness; ++j){
                  if ( audi < j && atoi(shyness[j]) > 0 ){
                       to_invite += (j - audi);
                       //cout << " Invite " << (j-audi) << " people. ";
                       audi += to_invite + atoi(shyness[j]);
                       //cout << " audi is "<< audi << endl;
                     }
                  else{
                       audi += atoi(shyness[j]);
    //                   cout << "shyness is " << j ;
      //                 cout << " audi is "<< audi << endl;
                       }
                 }
            cout << "Case #" << i << ": " << to_invite << endl;
	}
return 0;
}
