
#include<iostream>
#include<vector>
#include<math.h>
#define ull unsigned long long int
using namespace std;
vector<string> vec;
int n,j;


int main(){
        int t;cin>>t;
        for(int tt=1;tt<=t;tt++){
                int k,c,s;cin>>k>>c>>s;
                if(k==s){
                        cout<<"Case #"<<tt<<": ";
                        for(int i=1;i<=k;i++) cout<<i<<" ";
                        cout<<endl;
                 }
        }
        
	return 0;
}
