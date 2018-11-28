#include<iostream>
#include<vector>
using namespace std;

void bubble (vector<float>& a, int n){
	int pass, j;
	float tmp;
	bool xchange = true;
	for (pass = 1; pass < n && xchange == true; pass++){
		xchange = false;
		for (j=0; j < n-pass; j++){
			if (a[j] < a[j+1]){
				tmp = a[j]; a[j] = a[j+1]; a[j+1] = tmp;
				xchange = true;
			}
		}
	}
}


int main(){
	int cases,temp=1;
	cin>>cases;
	while(cases>0){
		int blocks,win1=0,win2=0,s1=0,s2=0;
		float tmp;
		vector<float> w1,w2;
		cin>>blocks;
		for(int i=0;i<blocks;i++){
			cin>>tmp;
			w1.push_back(tmp);
		}
		for(int i=0;i<blocks;i++){
			cin>>tmp;
			w2.push_back(tmp);
		}
		bubble(w1,blocks);
		bubble(w2,blocks);
		for(int i=0;i<blocks;i++){
			if(w1[s1]>w2[i]){
				win1++;
				s1++;
			}
			if(w2[s2]>w1[i]){
				win2++;
				s2++;
			}
		}
		cout<<"Case #"<<temp<<": "<<win1<<" "<<blocks-win2<<endl;
		cases--;temp++;
	}
}
