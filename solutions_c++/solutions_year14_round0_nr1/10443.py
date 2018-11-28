#include <iostream>
#include <vector>
using namespace std;
vector<int> intersection(vector<int> f, vector<int> b){
	vector<int> final;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(f[i]==b[j])
				final.push_back(f[i]);
		}
	}
	return final;
}
int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int ans1,ans2;
		cin>>ans1;
		int first[4][4],second[4][4];
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>first[j][k];
			}
		}
		cin>>ans2;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>second[j][k];
			}
		}
		ans1--;
		ans2--;
		//cout<<ans1<<"\t"<<ans2<<endl;
		vector<int> f,b;
		f.push_back(first[ans1][0]);
		f.push_back(first[ans1][1]);
		f.push_back(first[ans1][2]);
		f.push_back(first[ans1][3]);
		b.push_back(second[ans2][0]);
		b.push_back(second[ans2][1]);
		b.push_back(second[ans2][2]);
		b.push_back(second[ans2][3]);
		vector<int> final = intersection(f,b);
		if(final.size() == 1)
			cout<< "Case #"<<(i+1)<<": "<<final[0]<<endl;
		else if(final.size() == 0)
			cout<< "Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
		else if(final.size() > 1)
			cout<< "Case #"<<(i+1)<<": Bad magician!"<<endl;
	}
}


