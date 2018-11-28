#include<bits/stdc++.h>
using namespace std;


int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int temp, cs;
	cin>>temp;
	//	int temp, cs;
	for (cs = 1; cs <= temp; cs ++) {
		int i, j, k;
		
		cin>>i>>j>>k;
		if(j>k) swap(j,k);
		cout<<"Case #"<<cs<<": ";
		if (i==1) {
			cout<<"GABRIEL"<<endl;
		} else if (i==2) {
			if ((j*k)%2 == 0) {
				cout<<"GABRIEL"<<endl;
			} else {
				cout<<"RICHARD"<<endl;
			}
		} else if (i==3) {
			if ((j==3 || k==3) && (j!=1 && k!=1)) {
				cout<<"GABRIEL"<<endl;
			} else {
				cout<<"RICHARD"<<endl;
			}
		}
		else {
			if (k==4 &&(j==3||j==4))
				cout<<"GABRIEL"<<endl;
			else 
				cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
