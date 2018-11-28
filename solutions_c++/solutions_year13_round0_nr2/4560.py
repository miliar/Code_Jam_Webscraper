#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct Info{
	int x,y,height;
	Info(int x,int y,int height):x(x),y(y),height(height){};
	bool operator < (const Info &a)const {
		return this->height > a.height;
	}
};

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int N,M;
		cin>>N>>M;
		vector<vector<int> > board(N,vector<int>(M));
		for(int y=0;y<N;y++){
			for(int x=0;x<M;x++){
				cin>>board[y][x];
			}
		}
		vector<Info> infos;
		vector<bool> can_use_x(M,true);
		vector<bool> can_use_y(N,true);

		int min_height=100000000;
		for(int y=0;y<N;y++){
			for(int x=0;x<M;x++){
				min_height=min(min_height,board[y][x]);
				infos.push_back(Info(x,y,board[y][x]));
			}
		}
		sort(infos.begin(),infos.end());

		bool is_ok=true;
		vector<bool> bef_can_use_x=can_use_x;
		vector<bool> bef_can_use_y=can_use_y;

		for(int i=0;i<infos.size();i++){
			int x=infos[i].x,y=infos[i].y;
			if(i>0 && infos[i-1].height>infos[i].height){
				can_use_x=bef_can_use_x;
				can_use_y=bef_can_use_y;
			}
			if(!(can_use_x[x] || can_use_y[y])){//CAN NOT
				is_ok=false;
				break;
			}
			bef_can_use_x[x]=false;
			bef_can_use_y[y]=false;
		}
		if(is_ok){
			cout<<"Case #"<<t<<": "<<"YES"<<endl;
		}
		else{
			cout<<"Case #"<<t<<": "<<"NO"<<endl;
		}
	}
}