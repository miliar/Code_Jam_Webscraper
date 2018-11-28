//chiragjn
#include <iostream>
#include <vector>
#include <sstream>
#include <limits>
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define gibe_de_fast_io_b0ss ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
const ll mod = 1e9 + 7;
const ll INF = 0x7FFFFFFFFFFFFFFF/2;
vector<int> arr,arr2;
int main(){
    gibe_de_fast_io_b0ss;
    int t,k;
    cin>>t;
    string s;
    for(int T=1;T<=t;T++){
    	cin>>s>>k;
    	arr.clear();
    	arr2.clear();
    	for(int i=0;i<s.size();i++){
    		int z = (s[i]=='+')?1:0;
    		arr.pb(z);
    		arr2.pb(z);
    	}
    	int ans=INT_MAX,ans1=0,ans2=0;
    	//try forward
    	for(int i=0;i<s.size()-k+1;i++){
    		if(arr[i]==0){
    			ans1++;
    			for(int j=i,z=0;z<k;j++,z++){
    				arr[j] = (arr[j]==0)?1:0;
    			}
    		}
    	}
    	int anderson = 1, anderson2 = 1;
    	for(int x:arr){
    		anderson &= x;
    	}
    	if(anderson){
    		ans = min(ans, ans1);
    	}
    	//try backward
    	for(int i=s.size()-1;i>=k-1;i--){
    		if(arr2[i]==0){
    			ans2++;
    			for(int j=i,z=0;z<k;j--,z++){
    				arr2[j] = (arr2[j]==0)?1:0;
    			}
    		}
    	}
    	for(int x:arr2){
    		anderson2 &= x;
    	}
    	if(anderson2){
    		ans = min(ans, ans2);
    	}
    	if(ans == INT_MAX)
    		cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<"\n";
    	else
    		cout<<"Case #"<<T<<": "<<ans<<"\n";
    }
    return 0;
}