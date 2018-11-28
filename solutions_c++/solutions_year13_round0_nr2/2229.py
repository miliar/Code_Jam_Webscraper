#include<iostream>
#include<algorithm>

using namespace std;

int lawn[100][100];
int rmax[100],cmax[100];
int R,C,Lmax;

void input(){
	cin>>R>>C;
	Lmax=0;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cin>>lawn[i][j];
			Lmax=max(Lmax,lawn[i][j]);
		}
	}
	
	for(int i=0;i<R;i++){
		rmax[i]=0;
		for(int j=0;j<C;j++)
			rmax[i]=max(rmax[i],lawn[i][j]);
	}
	for(int j=0;j<C;j++){
		cmax[j]=0;
		for(int i=0;i<R;i++)
			cmax[j]=max(cmax[j],lawn[i][j]);
	}
	
}

bool cheak(){
	
	for(int l=1;l<=Lmax;l++){
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(lawn[i][j]==l&&l<rmax[i]&&l<cmax[j]){
					return false;
				}
			}
		}
	}
	
	return true;
}


int main(){
	
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		input();
		if(cheak())cout<<"Case #"<<testcase<<": YES"<<endl;
		else cout<<"Case #"<<testcase<<": NO"<<endl;
	}
	return 0;
}
