#include <iostream>
using namespace std;

int main(){
	int t,count_row_x,count_row_o,count_diag1_o,count_diag1_x,count_diag2_o,count_diag2_x;char a[4][4];
	cin>>t;bool flagx,flago,empty;int c=1;
	while(t--){
		// if(first) cout<<"\nCase #"<<c++<<": ";
		// else 
		cout<<"Case #"<<c++<<": ";
		int count_col_x[4]={0},count_col_o[4]={0};
		count_diag1_o=0;
		count_diag1_x=0;
		count_diag2_o=0;
		count_diag2_x=0;
		flagx=false;flago=false;empty=false;
		for(int i=0;i<4;i++){
			count_row_x=0;
			count_row_o=0;
			for(int j=0;j<4;j++){
				cin>>a[i][j];
				if(a[i][j]=='X'||a[i][j]=='T') {count_row_x++;count_col_x[j]++;}
				if(a[i][j]=='O'||a[i][j]=='T') {count_row_o++;count_col_o[j]++;}
				if(!empty&&a[i][j]=='.') empty=true;
				if(i==j) {if(a[i][j]=='X'||a[i][j]=='T') count_diag1_x++;if(a[i][j]=='O'||a[i][j]=='T') count_diag1_o++;}
				if(i+j==3) {if(a[i][j]=='X'||a[i][j]=='T') count_diag2_x++;if(a[i][j]=='O'||a[i][j]=='T') count_diag2_o++;}
			}
			if(count_row_x==4) {flagx=true;}
			else if(count_row_o==4) {flago=true;}
		}
		//cout<<count_diag1_o<<"  "<<count_diag1_x<<"  "<<count_diag2_o<<"  "<<count_diag2_x<<"  "<<count_row_x<<"  "<<count_row_o<<" ";

		for (int i = 0; i < 4; ++i){
			// cout<<count_col_o[i]<<" "<<count_col_x[i]<<" ";
			if(count_col_o[i]==4) {flago=true;break;}
			if(count_col_x[i]==4) {flagx=true;break;}
		}

		if(count_diag1_o==4||count_diag1_x==4||count_diag2_o==4||count_diag2_x==4) {
			if(count_diag1_o==4||count_diag2_o==4) {cout<<"O won";}
			if(count_diag1_x==4||count_diag2_x==4) {cout<<"X won";}
		}else{
			if(flagx||flago){
				if(flagx) cout<<"X won";else cout<<"O won";
			}else{
				if(empty) cout<<"Game has not completed";
				else cout<<"Draw";
			}
		}
		cout<<endl;
	}
}