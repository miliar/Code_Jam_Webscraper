#include<iostream>
#include<fstream>
#define cin fcin
#define cout fout
using namespace std;
ifstream fcin("datein.txt");
ofstream fout("dateout.txt");
int m[7][7];
int f[5];
int main(){
	int T;
	cin>>T;
	for(int w=1;w<=T;w++){
		int n;
		cin>>n;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)cin>>m[i+1][j+1];
		for(int k=1;k<=4;k++)f[k]=m[n][k];
		cin>>n;
        for( i=0;i<4;i++)
			for(int j=0;j<4;j++)cin>>m[i+1][j+1];
		int sum=0,now=-1;
		for(k=1;k<=4;k++)
			for(int j=1;j<=4;j++)
				if(m[n][j]==f[k]){
					now=f[k];
					sum++;
				}
				if(!sum)cout<<"Case #"<<w<<": Volunteer cheated!"<<endl;
				else if(sum>1)cout<<"Case #"<<w<<": Bad magician!"<<endl;
				else cout<<"Case #"<<w<<": "<<now<<endl;
				}
	return 0;
}

