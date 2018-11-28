#include<bits/stdc++.h>
#define ll long long

using namespace std;

const ll MOD = 1e9+7;
int arr[26];
bool flag[26];

int main(){
	int t,n,i,c;
	cin>>t;
	string ans,temp,temp1;
	
	for(c=1;c<=t;c++){
		cin>>n;
		for(i=0;i<n;i++)cin>>arr[i];
		int max=0;
		ans="";
		while(true){
			int max=0;
			temp="";
			for(i=0;i<n;i++)flag[i]=false;
			bool f1=true;
			for(i=0;i<n;i++){
				if(arr[i]!=1){
					f1=false;break;
				}
			}
			if(f1){
				temp1="";
				for(i=0;i<n;i++){
					if(arr[i]==1)temp1+=char(i+65);
				}
				//cout<<temp1<<endl;
				if(temp1.length()%2==0){
					for(i=0;i<temp1.length();i+=2){
						temp+=temp1[i];
						temp+=temp1[i+1];
						if(i+2!=temp1.length())temp+=' ';
					}
				}
				else{
					temp+=temp1[0];
					temp+=' ';
					for(i=1;i<temp1.length();i+=2){
						temp+=temp1[i];
						temp+=temp1[i+1];
						if(i+2!=temp1.length())temp+=' ';
					}
				}
				//cout<<temp<<endl;
				//break;
			}
			else{
				for(i=0;i<n;i++){
					if(arr[i]>max && temp==""){
						max=arr[i];
						flag[i]=true;
						temp=char(i+65);
					}
					else if(arr[i]>max){
						for(int j=0;j<temp.length();j++){
							flag[temp[j]-65]=false;
						}
						temp=char(i+65);
						flag[i]=true;
						max=arr[i];
					}
					else if(arr[i]==max && max!=0){
						temp+=char(i+65);
						flag[i]=true;
						max=arr[i];
					}
					if(temp.length()>2){
						flag[temp[0]-65]=false;
						temp=temp.substr(1);
					}
				}
			}
			
			if(temp.length()==0)break;
			if(ans=="")ans+=temp;
			else{
				ans+=' ';
				ans+=temp;
			}
			for(i=0;i<n;i++){
				if(flag[i])arr[i]--;
			}
			if(f1)break;
		}
		cout<<"Case #"<<c<<": ";
		cout<<ans<<endl;
	}
	return 0;
}
