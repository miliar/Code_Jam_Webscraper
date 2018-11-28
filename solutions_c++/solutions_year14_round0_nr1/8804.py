#include <bits/stdc++.h>
using namespace std;
int main ()
{
	int x1[4],x2[4],row1,row2,t;
	freopen ("myfile.txt","w",stdout);
	cin>>t;
	string empty;
	for(int i = 0; i < t; ++i){
		cin>>row1;
		getline(cin,empty);
		for(int j = 0; j < 4; ++j){
			if(j+1 == row1){
				for(int k = 0; k < 4; ++k) scanf("%d",&x1[k]);
				getline(cin,empty);}			
			else getline(cin,empty);
			}
		cin>>row2;
		getline(cin,empty);
		for(int j = 0; j < 4; ++j){
			if(j+1 == row2){
				for(int k = 0; k < 4; ++k) scanf("%d",&x2[k]);
				getline(cin,empty);}			
			else getline(cin,empty);
			}		
		sort(x1,x1+4);
		sort(x2,x2+4);
		int c = 0,f = 0;
		for(int h = 0; h<4;h++)
			for(int n = 0; n < 4; ++n)
				if(x1[h] == x2[n]) f = x1[h],++c;
		cout<<"Case #"<<(i+1)<<": ";		
		if(c > 1) 		cout<<"Bad magician!"<<endl;
		else if(c == 1) cout<<f<<endl;
		else if(c == 0) cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
