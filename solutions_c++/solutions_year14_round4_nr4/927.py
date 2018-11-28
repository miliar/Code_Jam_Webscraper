#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <queue>
#include <iomanip>
using namespace std;
int main(){
	long long t,te,i,j,k,y,m,n,ans1,ans2,x;
	ifstream f1;
	ofstream f2;
	f1.open("input.txt");
	f2.open("output.txt");
	f1>>t;
	for(te=0;te<t;te++){
		f1>>m>>n;
		string inp[m];
		for(i=0;i<m;i++)f1>>inp[i];
		ans1=0;
		ans2=0;
		for(i=0;i<(long long)round(pow(n,m));i++){
			vector<string>arr[n];
			for(k=0,j=i;k<m;k++,j/=n)
				arr[j%n].push_back(inp[k]);
			x=0;
			for(j=0;j<n;j++){
				if(arr[j].size()==0)continue;
				x++;
				int ma=0;
				for(k=0;k<arr[j].size();k++)ma=max(ma,(int)arr[j][k].size());	
				sort(arr[j].begin(),arr[j].end());
				x+=arr[j][0].size();
				for(k=1;k<arr[j].size();k++){
					for(y=0;y<arr[j][k].size();y++){
						if(y>=arr[j][k-1].size()||arr[j][k][y]!=arr[j][k-1][y])break;
					}
					x+=(arr[j][k].size()-y);
				}
			}
			if(x>ans1){
				ans1=x;
				ans2=0;
			}
			if(x==ans1)ans2++;
		}
		f2<<"Case #"<<1+te<<": "<<ans1<<" "<<ans2<<"\n";
		cout<<"Case #"<<1+te<<": "<<ans1<<" "<<ans2<<"\n";
	}
	return 0;
}
