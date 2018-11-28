#include <iostream>
#include <cstdio>
#include<fstream>
using namespace std;

#define ll long long int

int main() {
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	//scanf("%d",&t);
	fin>>t;
	
	for(int k=1; k<=t; ++k) {
		int ans1,ans2;
		int a[4][4],b[4][4];
		
		fin>>ans1;
		//scanf("%d",&ans1);
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j) {
				//cin>>a[i][j];
				fin>>a[i][j];
			}
		}
		
		//scanf("%d",&ans2);
		fin>>ans2;
		for(int i=0;i<4; ++i) {
			for(int j=0;j<4; ++j) {
				//cin>>b[i][j];
				fin>>b[i][j];
			}
		}
		
		int cnt1[17],cnt2[17];
		int res=0,val=-1;
		
		for(int i=0;i<17;++i) {
			cnt1[i]=0;
			cnt2[i]=0;
		}
		
		for(int i=0;i<4;++i) {
			cnt1[a[ans1-1][i]]++;
			cnt2[b[ans2-1][i]]++;
		}
		
		for(int i=0;i<17;++i) {
			if(cnt1[i] == 1 && cnt2[i]==1) {
				++res;
				val=i;
			}
		}
		
		if(res==1) {
			//printf("Case #%d: %d\n",k,val);
			fout<<"Case #"<<k<<": "<<val<<"\n";
		}
		else if(res >1) {
			//printf("Case #%d: Bad magician!\n",k);
			fout<<"Case #"<<k<<": Bad magician!\n";
		}
		else {
			//printf("Case #%d: Volunteer cheated!\n",k);
			fout<<"Case #"<<k<<": Volunteer cheated!\n";
		}
	}
	
	fin.close();
	fout.close();
	return 0;
}
