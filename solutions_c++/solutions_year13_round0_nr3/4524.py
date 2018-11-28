
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream cout ("B-small.out");
    ifstream cin ("B-small.in");
	int fairsquaretable[6]={0,1,4,9,121,484};
	int t=0;
	int n,m,ans=0;
	while(cin>>t){
	for(int cnt=0;cnt<t;cnt++){
		cin>>n>>m;
		for(int i=0;i<6;i++){
			if(fairsquaretable[i]<=m&&fairsquaretable[i]>=n)ans++;
		}
		cout<<"Case #"<<cnt+1<<": "<<ans<<endl;
		ans=0;
	}
	}
    return 0;
}
