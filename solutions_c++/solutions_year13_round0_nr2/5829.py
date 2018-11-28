#include <vector>
#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int n, now, pr,P, a[101][101], k,str[101], stolb[101], m;
void check(int l){
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			if(a[i][j] != str[i] && a[i][j] != stolb[j]){
				cout<<"Case #"<<l<<": "<<"NO"<<"\n";
				return;
			}
		}
	}
	cout<<"Case #"<<l<<": "<<"YES"<<"\n";
}
int main() {
    cin>>k;
	for(int z = 1; z <= k; z++){
		cin>>n>>m;
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
				cin>>a[i][j];
				str[i] = max(str[i],a[i][j]);
				stolb[j] = max(stolb[j],a[i][j]);
			}
		}
		check(z);
		for(int i = 1; i <= n; i++)str[i] = 0;
		for(int j = 1; j <= m; j++) stolb[j] = 0;
	}
    return 0;
}