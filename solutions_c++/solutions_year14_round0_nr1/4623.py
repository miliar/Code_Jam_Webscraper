#include<iostream>
using namespace std;
#include<fstream>
#include<ostream>
int a[5][5],b[5][5];
int main()
{
	ifstream fin("A-small-attempt2.in");  // 已有输入文件
    ofstream fout("output.txt");  //输出文件
    streambuf *cinbackup;  
    streambuf *coutbackup; 
    coutbackup= cout.rdbuf(fout.rdbuf());  //用 rdbuf() 重新定向
    cinbackup= cin.rdbuf(fin.rdbuf());  //用 rdbuf() 重新定向
	int tcase; cin>>tcase;
	int k=1;
	while(k<=tcase){
		int ans1; cin>>ans1;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
			}
		}
		int ans2; cin>>ans2;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>b[i][j];
			}
		}
		int cnt=0; int ai;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(a[ans1][i]==b[ans2][j]) { cnt++; ai=i; }
			}
		}
		cout<<"Case #"<<k++<<": ";
		if(cnt==1) cout<<a[ans1][ai]<<endl;
		if(cnt>1) cout<<"Bad magician!"<<endl;
		if(cnt==0) cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}