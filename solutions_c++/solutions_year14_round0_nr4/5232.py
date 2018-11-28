/*krypto...........................................jagsxi...!! */


#include<bits/stdc++.h>


using namespace std;
int main(){
int i,j,k,t,z=0,x,y,n;
double c,f,s=0.0,l=0.0,m=0.0;
cin>>t;
while(t--){
	vector<double>a,b;
    x=0,y=0;
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
           // cout<<"a - "<<y;
            //cout<<a[i]<<' '<<b[j]<<'\t';
        if(a[i]>b[j]){
            x++;
            j++;
          //  cout<<"yay"<<y;
        }
    }
    for(i=0,j=0;i<n;i++){ //   cout<<"b-"<<y;
        if(b[i]>a[j]){
            y++;
            j++;
            //cout<<"xbx"<<x;
        }
    }
    y=n-y;
    cout<<"Case #"<<z<<": "<<x<<' '<<y<<'\n';
}
return 0;
}
