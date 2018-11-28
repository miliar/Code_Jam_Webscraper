/*
 * p4cancer.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: rss
 */

#include <iostream>
using namespace std;
int T, X, R, C;
// i want to qualify and im not good enough at dp or however u solve this :c
int main() {
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>X>>R>>C;
		if (X==1) {
			cout<<"Case #"<<t<<": GABRIEL"<<endl;
			continue;
		}
		if (X==2) {
			if (R==1) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			} else if (R==2) {
				if (C==1) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			} else if (R==3) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			} else if (R==4) {
				if (C==1) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			}
		} else if (X==3) {
			if (R==1) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": RICHARD"<<endl;
			} else if (R==2) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": RICHARD"<<endl;
			} else if (R==3) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			} else if (R==4) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": RICHARD"<<endl;
			}
		} else if (X==4) {
			if (R==1) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": RICHARD"<<endl;
			} else if (R==2) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": RICHARD"<<endl;
			} else if (R==3) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			} else if (R==4) {
				if (C==1) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==2) cout<<"Case #"<<t<<": RICHARD"<<endl;
				else if (C==3) cout<<"Case #"<<t<<": GABRIEL"<<endl;
				else if (C==4) cout<<"Case #"<<t<<": GABRIEL"<<endl;
			}
		}
	}
	return 0;
}
