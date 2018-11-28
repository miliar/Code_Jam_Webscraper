#include <bits/stdc++.h>

using namespace std;
 
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> pii;
typedef vector< pii > vii;
typedef long long ll;
 
#define tcase int __t;cin >> __t; while( __t--)
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rp(i,b) fr(i,0,b)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define inf 1 << 32

void ch(vector<int>&v ,int& count,int temp){
	while(temp !=0){
		if(v[temp%10] == 0){
			v[temp%10]=1;
			count++;
		}
		temp=temp/10;
	}
	return;
}

int main(){
	int t,n,m=1;
	int count=0;
	long long int temp;
	vector<int> v(10);
	cin >> t;
	for(int j=0;j<t;j++){
		count=0;
		for(int i=0;i<10;i++){
			v[i]=0;
		}
		cin >> n;
		m=1;
		if(n!=0){
			while(1){
				temp=m*n;
				ch(v,count,temp);
				if(count==10){
					break;
				}
				m++;
			}	
			cout << "Case #"<<j+1<<": ";
			cout << temp <<endl;
		}
		else{
			cout << "Case #"<<j+1<<": ";
			cout << "INSOMNIA" <<endl;
		}
		
	}
	return 0;
}