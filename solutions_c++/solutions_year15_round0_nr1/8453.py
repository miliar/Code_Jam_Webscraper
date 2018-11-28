/*
 * =====================================================================================
 *
 *       Filename:  qa1.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/11/15 21:53:23
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>

using namespace std;


int main()
{
	int T,Smax;
	cin>>T;
	char* aus=0;
	for(int i=0;i<T;i++){
		cin>>Smax;
		aus=new char[Smax+1];
		cin>>aus;
		int standupCount=0;
		int inviteCount=0;
		for(int j=0;j<=Smax;j++){
			if(standupCount<j){
				inviteCount++;
				standupCount++;
			}	
			standupCount+=(aus[j]-'0');
		}
		cout<<"Case #"<<i+1<<": "<<inviteCount<<endl;
		delete aus;
		aus=NULL;
	}
}

