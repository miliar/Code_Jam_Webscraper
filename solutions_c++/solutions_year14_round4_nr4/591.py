#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
	
int main(){
	int TT;
	cin>>TT;


	int m;
	int n;
	int en=1;
	string str[1100];

	for(int T=1;T<=TT;++T){
		cin>>m>>n;
		for(int i=0;i<m;++i){
			cin>>str[i];
		}
		en=1;
		for(int i=0;i<m;++i){
			en*=n;
		}
		vector<string> v[110];
		int tmp;
		int count;
		int max_count=0;
		int cc=0;
		for(int i=0;i<en;++i){
			tmp=i;
			for(int k=0;k<n;++k)
				v[k].clear();
			for(int j=0;j<m;++j){
				v[tmp%n].push_back(str[j]);
				tmp/=n;
			}
			count=0;	
			for(int k=0;k<n;++k){
				//sort(v[k].begin(),v[k].end());
				vector<string> tmp;
				if(v[k].size()>0){
					tmp.push_back("");
					++count;
				}
				for(int j=0;j<v[k].size();++j){
					for(int l=1;l<=v[k][j].size();++l){
						string s2=v[k][j].substr(0,l);
						bool g=true;
						for(int p=0;p<tmp.size();++p){
							if(tmp[p]==s2)
								g=false;
						}
						if(g){
							++count;
							tmp.push_back(s2);
							//cout<<s2;
						}
					}
				}
				//cout<<endl;
			}
			//cout<<"=====\n";
			if(count>max_count){
				max_count=count;
				cc=1;
			}
			else if(count==max_count){
				++cc;
			}
		}
		int ans=max_count;
		cout<<"Case #"<<T<<": "<<ans<<" "<<cc<<"\n";



	}
	return 0;
}
