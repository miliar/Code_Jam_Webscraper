#include<iostream>
using namespace std;
int main(){
	
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int k = 0 ;
	string R = "RICHARD";
	string G = "GABRIEL";
	string arr[5][5]  ;
	arr[1][1] = "GRRR";// this is they will be glad and 
	arr[1][2] = "GGRR";//
	arr[1][3] = "GRRR";//
	arr[1][4] = "GGRR";
	arr[2][1] = "GGRR";
	arr[2][2] = "GGRR";
	arr[2][3] = "GGGR";
	arr[2][4] = "GGRR";
	arr[3][1] = "GRRR";
	arr[3][2] = "GGGR";
	arr[3][3] = "GRGR";
	arr[3][4] = "GGGG";
	arr[4][1] = "GGRR";
	arr[4][2] = "GGRR";
	arr[4][3] = "GGGG";
	arr[4][4] = "GGRG";	
	while(t--){
		++k;
		int r,c,x;
		cin>>x>>r>>c ;
		if(arr[r][c][x-1] == 'G' )
			cout<<"Case #"<<k<<": "<<G<<endl;
		else 
			cout<<"Case #"<<k<<": "<<R<<endl;
	}
}
