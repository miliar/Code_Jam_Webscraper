#include<fstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
struct node{
	int x;
	char y;
	node(int xx,char yy){
		x=xx;
		y=yy;
	}
	node(node& ls){
		x=ls.x;
		y=ls.y;
	}
};
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	//FILE *fin=fopen("in.txt","r");
	//FILE *fout=fopen("out.txt","w");
	int T,N,i,j;
	fin>>T;
	vector<node>a[101];
	string tmp;
	for(int times=1;times<=T;times++){
		fin>>N;
		for(i=1;i<=N;i++){
			
			fin>>tmp;
			a[i].clear();
			int count=1;
			for(j=1;j<tmp.length();j++){
				if(tmp[j]!=tmp[j-1]){
					a[i].push_back(node(count,tmp[j-1]));
					count=1;
				}
				else
					count++;
			}
			a[i].push_back(node(count,tmp[j-1]));
		}
		int n=a[1].size();
		vector<int>avg(n+1,0);
		bool flag=true;
		for(i=1;i<=N&&flag;i++){
			
			if(a[i].size()!=n){
				flag=false;
				break;
			}
			for(j=0;j<n;j++){
				//cout<<a[i][j].x<<' '<<a[i][j].y<<endl;
				//system("pause");
				if(a[i][j].y!=a[1][j].y){
					flag=false;
					break;
				}
				avg[j]+=a[i][j].x;
			}

		}
	
		if(!flag){
			fout<<"Case #"<<times<<": "<<"Fegla Won\n";
			//cout<<"Case #"<<times<<": "<<"Fegla Won\n";
			continue;
		}
		int ans=0;
		for(i=0;i<n;i++)
			avg[i]/=N;
		for(i=1;i<=N;i++){
			for(j=0;j<n;j++){
				ans+=abs(avg[j]-a[i][j].x);
			}
		}
		fout<<"Case #"<<times<<": "<<ans<<endl;
		//cout<<"Case #"<<times<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
	//fclose(fin);
	//fclose(fout);
	return 0;
}