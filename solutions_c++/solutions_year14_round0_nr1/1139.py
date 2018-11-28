#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <string.h>

using namespace std;

int mat[20];

int main() {
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++) {
		memset(mat,0,sizeof(mat));
		for(int i=0;i<2;i++) {
			int row;
			int temp;
			cin>>row;
			for(int j=0;j<4;j++) {
				for(int k=0;k<4;k++) {
					cin>>temp;
					if(j == row-1) {
						mat[temp]++;
					}
				}
			}
		}
		int ct=0;
		int ind=0;
		for(int i=1;i<=16;i++) {
			if(mat[i] == 2) {
				ct++;
				ind = i;
			}
		}
		if(ct > 1) {
			cout<<"Case #"<<ii<<": "<<"Bad magician!"<<endl;
		} else if(ct == 1) {
			cout<<"Case #"<<ii<<": "<<ind<<endl;
		} else {
			cout<<"Case #"<<ii<<": "<<"Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
