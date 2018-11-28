#include<fstream>
#include<vector>

using namespace std;

void seeDigits(int num, vector<int> &vis){
	while(num){
		int rem=num%10;
		num /= 10;
		if(vis[rem]==0)
			vis[rem]=1;
	}
}

bool allSeen(vector<int>vis){
	for(int i=0;i<10;i++)
		if(vis[i]==0)
			return false;
	return true;
}

int main(){
	ifstream fin("inp.txt");
	ofstream fout("op.txt");
	int t,n;
	fin>>t;
	for(int c=1;c<=t;c++){
		fin>>n;
		fout<<"Case #"<<c<<": ";
		if(n==0)
			fout<<"INSOMNIA\n";
		else{
			vector<int>vis(10,0);
			int cur=n;
			seeDigits(cur,vis);
			while(!allSeen(vis)){
				cur += n;
				seeDigits(cur,vis);
			}
			fout<<cur<<"\n";
		}
	}
}