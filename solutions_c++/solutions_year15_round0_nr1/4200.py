#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		int N;
		cin>>N;
		int A[N+1];
        string s;
        cin>>s;
        for(int i=0 ;i<=N; i++)
              A[i] = s[i]-'0';
        
        int ans=0,tot=A[0];
        for(int i=1; i<=N; i++){
            int reqd = i;
            //cout<<"reqd :"<<reqd<<" ";
            if(tot >= reqd){
                tot+=A[reqd];
            }else{
                int t = reqd-tot;
                ans += t;
                tot += A[reqd];
                tot += t;
            }
            //cout<<"tot so far :"<<tot<<" addition so far :"<<ans<<endl;
        }
		cout<<"Case #"<<x<<": ";
		cout<<ans<<endl;
		
		}
	return 0;
	}
	
