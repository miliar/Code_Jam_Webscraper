#include <iostream> 
#include <string> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <vector> 
#include <string.h> 
#include <stdio.h> 
#include <math.h> 
#include <sstream> 

using namespace std; 
int t;
int main(){
	cin>>t;
	for(int i=0 ; i<t ; i++){
		int n,m;
		cin>>n>>m;
		int a[100][100];
		for(int j=0 ; j<n ; j++){
			for(int k=0 ; k<m ; k++){
				cin>>a[j][k];
			}
		}
		// cout<<"oh yeah"<<endl;
		string status = "YES";
		for(int j=0 ; j<n ; j++){
			for(int k=0 ; k<m ; k++){
				int hor = 0;
				int ver = 0;
				for(int right=k ; right<m ; right++){
					if(a[j][right] > a[j][k])
						hor = 1;
				}
				for(int left=k ; left>=0 ; left--){
					if(a[j][left] > a[j][k])
						hor = 1;
				}
				for(int down=j ; down<n ; down++){
					if(a[down][k] > a[j][k])
						ver = 1;
				}
				for(int up=j ; up>=0 ; up--){
					if(a[up][k] > a[j][k])
						ver = 1;
				}
				if(hor + ver == 2)
					status = "NO";
			}
		}
		cout<<"Case #"<<i+1<<": "<<status<<endl;
	}

return 0; 
}