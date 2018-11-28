#include <iostream>
#include <algorithm>
#include <vector>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
	int cases;cin>>cases;
	int row1,row2,t;
	for(int caseI=1;caseI<=cases;caseI++){
		vector<int> p1[4],p2[4];
		cin>>row1;row1--;
		rep(i,4) rep(j,4) {cin>>t;p1[i].push_back(t);}
		cin>>row2;row2--;
		rep(i,4) rep(j,4) {cin>>t;p2[i].push_back(t);}
		vector<int> p3;
		rep(i,4) p3.push_back(p1[row1][i]);
		rep(i,4) p3.push_back(p2[row2][i]);
		sort(p3.begin(),p3.end());
		int last=-1,t=-1,n=0;
		// rep(i,8) cout<<p3[i]<<" ";cout<<endl;
		rep(i,8) if(p3[i]==last){n++;t=last;}else {last=p3[i];}

		cout<<"Case #"<<caseI<<": ";
		if(n==1) cout<<t<<endl;
		else if(n>1) cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
