#include <fstream>

using namespace std;

ifstream cin ("file1.in");
ofstream cout("file1.out");

int main(){
	int t=0;
	cin >> t;
	int n=0;
	int ans=0;
	int to=0;
	for( int j=0;j<t;j++){
		cin >> n;
		ans=0;
		to=0;
		for( int i=0;i<=n;i++){
			if( to < i ){
				ans+=i-to;
				to=i;
			}
			char c;
			cin >> c;
			int a=int(c)-48;
			to+=a;
		}
		cout << "Case #" << j+1 << ": " << ans << endl;	
	}
	return 0;
}
