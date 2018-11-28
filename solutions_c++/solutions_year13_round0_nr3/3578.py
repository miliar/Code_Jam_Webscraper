#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;
bool ispalindrom(int num){
	char str[8];
	itoa ( num,str,10 );
	int len = strlen(str);
	int i=0,j=len-1;
	bool ispalin=true;
	while(i<j){
		if( str[i] != str[j] ){
			ispalin=false;
			break;
		}
		++i;--j;
	}
	return ispalin;
}
int main() {
	int t;
	cin>>t;
	int start,end;
	for(int i=1;i<=t;++i){
		cin>>start>>end;
	//	cout<<start<<end<<endl;
		int count=0;
		for(int j=start;j<=end;++j){
			if( ispalindrom(j) ){
				int root=sqrt(j);
				if( root*root == j ){
					if( ispalindrom(root) )
						++count;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
