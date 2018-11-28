#include<bits/stdc++.h>

using namespace std;
int main(){
	int T,n,a,caso=1;
	vector<int>v,v2;
	cin>>T;
	while(T--){
		string s;
		cin>>n;
		v.clear();v2.clear();
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++){
				cin>>a;
				if(i == n)v.push_back(a);
			}
		cin>>n;
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++){
				cin>>a;
				if(i == n)v2.push_back(a);
			}
		bool b=0;
		int t=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(v[i]==v2[j]){t++;a=v[i];}
			}
		}
					
				if(t==1){
					b=1;
			
				}else{
					if(t==0)s="Volunteer cheated!";
					else s="Bad magician!";
				}	
		
		if(b){
			printf("Case #%d: %d\n",caso++,a);
		}else{
			printf("Case #%d: %s\n",caso++,s.c_str());
		}
		
	}

 return 0;
}
