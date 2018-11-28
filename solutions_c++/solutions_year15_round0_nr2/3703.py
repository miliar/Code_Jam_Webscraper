#include <fstream>
#include <vector>
#include <algorithm>

#define Max 1000

using namespace std;

int t=0;
int n=0;

ifstream cin ("1.in");
ofstream cout ("1.out");

int arr[Max];

int main(){
	cin >> t;
	for( int i=0;i<t;i++){
		cin >> n;
		for( int j=0;j<n;j++)
			cin >> arr[j];
		
		int ans=Max;
		for( int j=1;j<1000;j++){
			int ans1=0;
			for( int k=0;k<n;k++){
				ans1+=arr[k]/j-1;
				if( arr[k] % j != 0 )
					ans1++;
			}
			ans=min(ans1 + j ,ans);
		}
		cout << "Case #" << i+1 << ": ";
		cout << ans << endl;
	}
	return 0;
}
