#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

bool Possibility(int h,int tmp[100][100],int N,int M){
	int lawn[100][100];
	for(int n=0;n<N;n++){
		for(int m=0;m<M;m++){
			lawn[n][m]=tmp[n][m];
		}
	}
	bool chk=true;
	for(int n=0;n<N;n++){
		int x=0;
		for(int m=0;m<M;m++)
			if(lawn[n][m]<=h)
				x++;
		if(x==M)
			for(int m=0;m<M;m++)
				lawn[n][m]=0;
	}
	for(int m=0;m<M;m++){
		int x=0;
		for(int n=0;n<N;n++)
			if(lawn[n][m]<=h)
				x++;
		if(x==N)
			for(int n=0;n<N;n++)
				lawn[n][m]=0;
	}
	for(int n=0;n<N;n++)
		for(int m=0;m<M;m++)
			if(lawn[n][m]==h)
				chk=false;
	return chk;
}

int main(){
	ifstream inp;
	ofstream out;
	out.open("d:/out.txt");
	inp.open("d:/a.in");
	int T;
	inp>>T;
	for(int i=1;i<=T;i++){
		vector<int> H;
		int n,m;
		inp>>n>>m;
		int lawn[100][100];
		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				inp>>lawn[j][k];
				//cout<<lawn[j][k]<<' ';
				bool chk=true;
				for(int l=0;l<H.size();l++)
					if(H.at(l)==lawn[j][k])
						chk=false;
				if(chk)
					H.push_back(lawn[j][k]);
			}	
			//cout<<endl;
		}
		sort(H.begin(),H.end());
		bool Possible=true;
		for(int j=H.at(0);j<=H.at(H.size()-1);j++)
			if(!Possibility(j,lawn,n,m)){
				Possible=false;
				break;
			}else{
				for(int k=0;k<n;k++){
					for(int l=0;l<m;l++){
						if(lawn[k][l]<=j)
							lawn[k][l]=j+1;
					}
				}
			}
		cout<<"Case #"<<i<<": "<<((Possible)?"YES":"NO")<<endl;
		out<<"Case #"<<i<<": "<<((Possible)?"YES":"NO")<<endl;
		//system("pause");
		//system("cls");
	}
	system("pause");
	return 0;
}