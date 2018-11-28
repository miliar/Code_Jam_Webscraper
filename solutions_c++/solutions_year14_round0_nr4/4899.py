#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
int i,j,t,z=0,x,y,n;
cin>>t;
while(t--){
	vector<double>a,b; 
    x=0;
	y=0;
    z++;
   cin>>n;
   double a1[n],b1[n];
    for(i=0;i<n;i++){
        cin>>a1[i];
		a.push_back(a1[i]);
    }
    for(i=0;i<n;i++){
        cin>>b1[i];
        b.push_back(b1[i]);
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
     for(i=0,j=0;i<n;i++){
        if(a[i]>=b[j]){
            x++;
            j++;
        }
    }
    for(i=0,j=0;i<n;i++){
	        if(b[i]>=a[j]){
            y++;
			j++;
        }
    }
    y=n-y;
    cout<<"Case #"<<z<<": "<<x<<' '<<y<<'\n';
}
return 0;
}
