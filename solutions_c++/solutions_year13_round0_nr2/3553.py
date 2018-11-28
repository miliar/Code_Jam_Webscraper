#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int ch[100][100];
int main()
{
	FILE *fp,*fp_;
	freopen_s(&fp,"data.in","r",stdin);
	freopen_s(&fp_,"data.out","w",stdout);
	int T,N,M;
	cin>>T;
	for(int k=0;k<T;k++){
		bool to_break;
		cin>>N>>M;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				cin>>ch[i][j];
		for(int i=0;i<N;i++){
			to_break=false;
			for(int j=0;j<M;j++){
				bool x_break=false,y_break=false;
				int temp=ch[i][j];
				for(int r=0;r<M;r++){
					if(ch[i][r]>temp)
						x_break=true;
				}
				for(int r=0;r<N;r++){
					if(ch[r][j]>temp)
						y_break=true;
				}
				if(x_break&&y_break){
					cout<<"Case #"<<k+1<<":"<<" NO"<<endl;
					to_break=true;
					break;
				}
			}
			if(to_break)
				break;
		}
		if(!to_break)
			cout<<"Case #"<<k+1<<":"<<" YES"<<endl;
	}
	fcloseall();
	return 0;
}