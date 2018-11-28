#include <iostream>
#include <iomanip>
#include <sstream>
#include <utility>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <assert.h>
using namespace std;

int main()
{
    //freopen("c:/loadfiles/codejam/input.txt", "r", stdin);
    freopen("c:/loadfiles/downloads/A-small.in","r",stdin);
	freopen("c:/loadfiles/codejam/outputCPP.txt", "w", stdout);
    int trials;
    cin >> trials;
    for (int trial = 1; trial <= trials; ++trial) {
		vector<string>  lines;
		int n;
		printf("Case #%d: ", trial);
		cin>>n;
		string tmpl0;
		vector<vector<int> > allCounts;
		bool broken=false;
		for(int i=0;i<n;i++){
			string line;
			cin>>line;
			lines.push_back(line);
			string last="/";
			string tmpl="";
			vector<int> counts;
			for(int j=0;j<(int)line.length();j++){
				if(last[0]!=line[j]){
					last=line[j];
					tmpl=tmpl+last;
					counts.push_back(1);
				}else{
					counts[(int)counts.size()-1]++;
				}
			}
			allCounts.push_back(counts);
			if(i==0)tmpl0=tmpl;
			if(tmpl0!=tmpl){
				broken=true;
				break;
			}
		}
		if(broken){
			cout<<"Fegla Won";
			cout<<"\n";
		}else{
		//	cout<<tmpl0<<" ";
			long long cost=0;
			for(int i=0;i<(int)tmpl0.length();i++){
				long long minCost=9999999999;
				for(int j=0;j<n;j++){
			//		cout<<endl;
					long long tCost=0;
					for(int k=0;k<n;k++){
						tCost+=(int)abs(allCounts[k][i]-allCounts[j][i]);
	//					cout<<" "<<tCost;
					}
					minCost=min(minCost,tCost);
		//			cout<<endl<<minCost<<endl;
				}
				cost+=minCost;
			}
			cout<<" "<<cost;
			printf("\n");
			
		}
	}
    
    return 0;
}
