#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main(void)
{
	ifstream fin;
	fin.open("A-small-attempt0.in");
	ofstream fout;
	fout.open("A-small-attempt0.out");
	
	int t;
	fin>>t;
	
	int n;
		
	for(int i=0;i<t;i++)
	{
		fin>>n;
		string tmp;
		vector<string> s;
		vector<string> ch;
		vector<vector<int> > ct;
		for(int m=0;m<n;m++){
			fin>>tmp;
			s.push_back(tmp);
			
			char pre='0';
			int count=1;
			string cht="";
			vector<int> ctt;
			
			for(int p=0;p<tmp.size();p++) {
				if(tmp[p]!=pre){
					if(p!=0){
						cht+=pre;
						ctt.push_back(count);
						count=1;
					}
					pre=tmp[p];
				}else count++;
			}
			if(count>0) {cht+=pre;ctt.push_back(count);}
			ch.push_back(cht);
			ct.push_back(ctt);
		}
				
		fout<<"Case #"<<i+1<<": ";
		
		bool flag=true;
		
		for(int m=1;m<n;m++){
			if(ch[m]!=ch[0]) {fout<<"Fegla Won"<<endl;flag=false;}
		}
		
		if(flag){
		
		
		int row=ct.size();
		int col=ct[0].size();
		
		int ave[col];
		for(int b=0;b<col;b++) ave[b]=0;
		
		for(int a=0;a<row;a++){
			for(int b=0;b<col;b++){
				ave[b]=ave[b]+ct[a][b];
			}
		}
		
		for(int b=0;b<col;b++) ave[b]/=row;
		
		int ret=0;
		
		for(int a=0;a<row;a++){
			for(int b=0;b<col;b++){
				ret+=abs(ave[b]-ct[a][b]);
			}
		}
		
		fout<<ret<<endl;
		
		}
				
	}
	return 0;
}