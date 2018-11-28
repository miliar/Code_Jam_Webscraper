#include <iostream>
#include <string>
#include <vector>
using std::vector;
using std::string;


int main(void){
	using namespace std;
	
	int dr[]={-1,01,00,00,};
	int dc[]={00,00,-1,-1,};
	int f[]={0,2,};
	int t[]={1,3,};
	int T;cin>>T;
	for(int X=1;X<=T;X++){
		int n;cin>>n;
		int m;cin>>m;
		int lawn[n*m];
		for(int row=0;row<n;row++){
			for(int col=0;col<m;col++){
				cin>>lawn[row*m+col];
			}
		}
		//
		int rowmax[n];
		for(int row=0;row<n;row++){
			rowmax[row]=lawn[row*m];
			for(int col=1;col<m;col++){
				if(rowmax[row]<lawn[row*m+col]){
					rowmax[row]=lawn[row*m+col];
				}
			}
		}
		int colmax[n];
		for(int col=0;col<m;col++){
			colmax[col]=lawn[col];
			for(int row=1;row<n;row++){
				if(colmax[col]<lawn[row*m+col]){
					colmax[col]=lawn[row*m+col];
				}
			}
		}
		bool flag=true;
		for(int row=0;row<n;row++){
			for(int col=0;col<m;col++){
				if(lawn[row*m+col]<rowmax[row]&&lawn[row*m+col]<colmax[col]){
					flag=false;
					goto ex;
				}
			}
		}
		ex:
		string result="";
		if(flag){
			result="YES";
		}else{
			result="NO";
		}
		//
		cout<<"Case #"<<X<<": "<<result<<endl;
	}
	cout.flush();
	cerr.flush();
	return 0;
}
