#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main(){
	ofstream fout ("solution.txt");
	int t;cin>>t;
	int p[101][101], a[101][101];
	for(int i (0);i!=t;++i){
		int x, y;cin>>x>>y;
		
		for(int j (0);j!=x;++j){
			for(int k (0);k!=y;++k){
				cin>>p[j][k];
				a[j][k]=100;
			}
		}
		
		for(int j (0);j!=x;++j){
			int maks=-1;
			for(int k (0);k!=y;++k){
				maks=max(p[j][k], maks);
			}
			for(int k (0);k!=y;++k){
				if(a[j][k]>maks)a[j][k]=maks;
			}
			
		}
		
		for(int k (0);k!=y;++k){
			int maks=-1;
			for(int j (0);j!=x;++j){
				maks=max(p[j][k], maks);
			}
			for(int j (0);j!=x;++j){
				if(a[j][k]>maks)a[j][k]=maks;
			}
			
		}
		bool ali=1;
		for(int j (0);j!=x;++j){
			for(int k (0);k!=y;++k){
				if(a[j][k]!=p[j][k])ali=0;
			}
			
		}
		
		
		fout<<"Case #"<<i+1<<": ";
		if(ali)fout<<"YES";
		else fout<<"NO";
		fout<<endl;
		
		
		
	}
}
