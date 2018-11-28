#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <limits.h>

using namespace std;

int main(){
	int t,n;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		bool possible=true;
		vector<string> str;
		vector<vector <int> > hints;
		for(int j=0;j<n;j++){
			hints.push_back(std::vector<int>());
			string tmp;
			cin>>tmp;
			int n=1;
			char last=tmp[0];
			for(int k=1; k<tmp.size();k++){
				if(last!=tmp[k]){
					hints[j].push_back(n);
					n=1;
				}
				else{
					n++;
				}
				last=tmp[k];
			}
			hints[j].push_back(n);

			for(int k=1;;k++){
				if(tmp.begin()+k == tmp.end())
					break;
				if(tmp[k]==tmp[k-1]){
					tmp.erase(tmp.begin()+k);
					k--;
				}
			}
			str.push_back(tmp);

			if(j!=0 && str[j].compare(str[j-1])!=0){
				cout<<"Case #"<<i+1<<": "<<"Fegla Won\n";
				possible=false;
				break;
			}
		}

		// if(possible){
		// 	int min=INT_MAX;
		// 	for(int x=0;x<hints.size();x++){
		// 		int sum=0;
		// 		for(int y=0;y<hints.size();y++){
		// 			if(x==y)
		// 				continue;

		// 			for(int k=0;k<hints[x].size();k++){
		// 				sum+=abs(hints[x][k]-hints[y][k]);
		// 			}
		// 		}

		// 		if(sum<min)
		// 				min=sum;
		// 	}

		// 	cout<<"Case #"<<i+1<<": "<<min<<"\n";
		// }

		if(possible){
			int sum=0,tmp;
			for(int k=0;k<hints[0].size();k++){
				int max=0;
				for(int x=0;x<hints.size();x++){
					for(int y=x;y<hints.size();y++){
						tmp=abs(hints[x][k]-hints[y][k]);
						if(max<tmp)
							max=tmp;
					}
				}
				sum+=max;
			}

			cout<<"Case #"<<i+1<<": "<<sum<<"\n";
		}

	}
}