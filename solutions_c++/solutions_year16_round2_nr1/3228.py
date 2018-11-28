#include<iostream>
#include<string>
using namespace std;

int carr[27],narr[10];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;cin>>t;for(int x=1;x<=t;x++){
		string s;cin>>s;
		for(int i=0;i<s.size();i++){
			int n;n=s[i]-'A'+1;carr[n]++;
		}
		narr[0]+=carr[26];	carr[5]-=carr[26];	carr[18]-=carr[26];	carr[15]-=carr[26];	carr[26]-=carr[26];
		narr[2]+=carr[23];	carr[20]-=carr[23];	carr[15]-=carr[23];	carr[23]-=carr[23];
		narr[4]+=carr[21];	carr[6]-=carr[21];	carr[15]-=carr[21];	carr[18]-=carr[21];	carr[21]-=carr[21];
		narr[6]+=carr[24];	carr[19]-=carr[24];	carr[9]-=carr[24];	carr[24]-=carr[24];
		narr[8]+=carr[7];	carr[5]-=carr[7];	carr[9]-=carr[7];	carr[8]-=carr[7];	carr[20]-=carr[7];	carr[7]-=carr[7];
		narr[1]+=carr[15];	carr[14]-=carr[15];	carr[5]-=carr[15];	carr[15]-=carr[15];
		narr[3]+=carr[8];	carr[20]-=carr[8];	carr[18]-=carr[8];	carr[5]-=2*carr[8];	carr[8]-=carr[8];
		narr[5]+=carr[6];	carr[9]-=carr[6];	carr[22]-=carr[6];	carr[5]-=carr[6];	carr[6]-=carr[6];
		narr[7]+=carr[19];	carr[19]-=carr[19];
		narr[9]+=carr[9];	carr[9]-=carr[9];
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<10;i++){
			for(int j=0;j<narr[i];j++){
				cout<<i;
			}
			narr[i]=0;
		}
		cout<<endl;
	}
	return 0;
}

