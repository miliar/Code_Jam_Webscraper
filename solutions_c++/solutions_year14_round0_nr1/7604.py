#include <iostream>
#include <cstring>
#include <vector>
#include <fstream>
using namespace std;
#define pb push_back
int a1[4][4],a2[4][4];
int main(){
	int tst=1,T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	while(tst<=T){
		int N1;
		cin>>N1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)cin>>a1[i][j];
		int N2;
		cin>>N2;
		for(int i=0;i<4;i++)	
			for(int j=0;j<4;j++)cin>>a2[i][j];
		vector<int>vec;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				if(a1[N1-1][i]==a2[N2-1][j])vec.pb(a1[N1-1][i]);
			}
		cout<<"Case #"<<tst<<": ";
		if(vec.size()==0){
			cout<<"Volunteer cheated!";
		}else if(vec.size()>1){
			cout<<"Bad magician!";
		}else{
			cout<<vec[0];
		}cout<<endl;
		tst++;
	}
	return 0;
}
