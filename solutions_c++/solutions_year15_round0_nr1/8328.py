#include <bits/stdc++.h>

using namespace std;

inline string IS(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int SI(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}

int A[1005],a,b,ans,ans1;
string s;

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	
	cin>>a;
	for(int i=0 ; i<a ; i++){
		cin>>b;
		cin>>s;
		for(int j=0 ; j<s.length() ; j++){
			if(j==0){
				ans=s[j]-48;
				
			}
			else{
				if(j>ans && s[j]>48){
					
					ans1+= j-ans;
					ans+= j-ans;
				}
				if(ans>=j){
					ans+= s[j]-48;
				}
			}
			
		}	
		cout<<"Case #"<<i+1<<": "<<ans1<<endl;
		ans=ans1=0;
	}
	

}
