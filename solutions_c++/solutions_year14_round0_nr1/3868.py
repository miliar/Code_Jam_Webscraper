#include <fstream>
#include <vector>

using namespace std;

ifstream cin("test.in");
ofstream cout("test.out");

#define M 20

int a[M], f[M][M];
vector<int> ans;

void read(void){
	for (int i=0; i<M; ++i)
		a[i]=0;
		
	ans.clear();
	
	for (int j=0; j<2; ++j){
		int x;
		cin>>x;
		
		for (int i=1; i<=4; ++i)
		for (int k=1; k<=4; ++k)
		cin>>f[i][k];
		
		for (int k=1; k<=4; ++k)
		a[f[x][k]]++;
	}
	
	for (int i=1; i<=16; ++i)
	if (a[i]==2)
	ans.push_back(i);
	
	if (ans.size()==1){
		cout<<ans[0]<<"\n";
		return;
	}
	
	if (ans.size()==0){
		cout<<"Volunteer cheated!\n";
		return;
	}
	
	cout<<"Bad magician!\n";
}

void kill(void){
	
}

int main(){
	int t;
	cin>>t;
	for (int i=1; i<=t; ++i){
		cout<<"Case #"<<i<<": ";
		read();
		kill();
	}
	return 0;
}
