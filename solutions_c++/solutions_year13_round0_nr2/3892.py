#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out_b.txt","w",stdout);

	int t,n,m;
	cin>>t;
	
	int arr[102][102];
		
	for(int p=1;p<=t;p++){
		cout<<"Case #"<<p<<": ";
		cin>>n>>m;
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>arr[i][j];
			}	
		}
		int fg=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				for(int x=0;x<n;x++){
					if(arr[x][j]>arr[i][j]){
			            x=1;
			            for(int x=0;x<m;x++)
			            	if(arr[i][x]>arr[i][j])
           					 	fg = 1;
			            break;
        			}
    			} 
				if(fg) break; 
        	}
        	if(fg) break;
		}
		if(fg) cout<<"NO\n";
		else cout<<"YES\n";
	}

	return 0;
	
}



