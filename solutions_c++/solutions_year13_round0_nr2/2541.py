#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<map>
using namespace std;

int findNum(vector<int> v, int num){
	int i;
	for(i=0; i<v.size(); i++){
		if(v[i]==num)
			return i;
	}
	return i;
}

int main()
{	
	int t; 
	cin>>t;
	for(int k=1; k<=t; k++){
		int row, col;
		cin>>row>>col;
		int i, j;
		vector< vector<int> > in;
		vector< vector<int> > my;
		vector<int> rowMax(row);
		vector<int> colMax(col);
		//Input Array
		in.resize(row); 	
		for(i=0; i<row; i++){
			in[i].resize(col);
			for(j=0; j<col; j++){
				cin>>in[i][j];
			}
		}
		//My Array
		my.resize(row); 
		for(i=0; i<row; i++){
			my[i].resize(col);
			for(j=0; j<col; j++){
				my[i][j]=101;
			}
		}
		//ROW MAX
		for(i=0; i<row; i++){	
			int max=0;
			for(j=0; j<col; j++){
				if(in[i][j]>max)
					max=in[i][j];
			}
			rowMax[i]=max;
		}
		//COL MAX
		for(i=0; i<col; i++){
			int max=0;
			for(j=0; j<row; j++){
				if(in[j][i]>max)
					max=in[j][i];
			}
			colMax[i]=max;
		}
		//COLUMN Calculation
		for(i=0; i<col; i++){
			for(j=0; j<row; j++){
				if(my[j][i]>colMax[i])
					my[j][i]=colMax[i];
			}
		}
		//ROW Calculation
		for(i=0; i<row; i++){
			for(j=0; j<col; j++){
				if(my[i][j]>rowMax[i])
					my[i][j]=rowMax[i];
			}
		}
		//Compare
		int status=1;
		for(i=0; i<row; i++){
			for(j=0; j<col; j++){
				if(my[i][j]!=in[i][j]){
					status=0;
					break;
				}
			}
			if(status==0)
				break;
		}
		
		if(status==0)
			cout<<"Case #"<<k<<": "<<"NO"<<endl;
		else
			cout<<"Case #"<<k<<": "<<"YES"<<endl;
	}
	return 0;
}