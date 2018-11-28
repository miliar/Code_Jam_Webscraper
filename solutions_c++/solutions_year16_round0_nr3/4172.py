#include<iostream>
#include<math.h>
#include<queue>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;

long long findDivisor(long long a){
	if(a==1||a==0)
		return 0;
	int lim=sqrt(a);
	for(int i=2;i<=lim;++i){
		if(a%i==0)
			return i;
	}
	return 0;
}

int main(){
	ofstream fout("ans3.txt");
	ifstream fin("inp3.IN");
	int t,n,j;
	fin>>t;
	int tt=0;
	while(tt++!=t){
	    fin>>n>>j;
        fout<<"Case #"<<tt<<":\n";
		queue<string> q;
		int complete=0;
		string base="1",cur;
		for(int i=2;i<n;++i)
			base=base+"0";
		base=base+"1";
		cur=base;
			for(int i=2;i<=10;++i){//loop for all bases
				long long div[9];

				long long num=0,mult=1;
				for(int b=n-1;b>=0;--b){
					int dig=cur[b]-'0';
					num+=(dig*mult);
					mult=mult*i;
				}
				long long verdict=findDivisor(num);
				if(verdict==0)
					break;
				else
					div[i-2]=verdict;
				if(i==10){
					fout<<num<<" ";
					for(int ctr=0;ctr<9;++ctr)
						fout<<div[ctr]<<" ";
					fout<<"\n";
					++complete;
				}
			}
		
		//check for types 101,11,1000001 here only

		q.push("1");

		while(complete<j){
			string last=q.front();
			q.pop();
			int mid=last.size();
			cur="1";
			for(int i=0;i<n-2-mid;++i)
				cur=cur+"0";
			cur=cur+last+"1";
			q.push(last+"0");
			q.push(last+"1");
			//check if cur satisfies prime in all bases

			
			for(int i=2;i<=10;++i){//loop for all bases
				long long div[9];

				long long num=0,mult=1;
				for(int b=n-1;b>=0;--b){
					int dig=cur[b]-'0';
					num+=(dig*mult);
					mult=mult*i;
				}
				long long verdict=findDivisor(num);
				if(verdict==0)
					break;
				else
					div[i-2]=verdict;
				if(i==10){
					fout<<num<<" ";
					for(int ctr=0;ctr<9;++ctr)
						fout<<div[ctr]<<" ";
					fout<<"\n";
					++complete;
				}
			}

		}
		

	}

}
