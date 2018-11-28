#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(){
//    FILE *fin = freopen("A-small.in", "r", stdin);
//	assert( fin!=NULL );
//	FILE *fout = freopen("A-small.out", "w", stdout);

  ifstream fin;
	fin.open("A-small-attempt2.in");
    ofstream fout;
	fout.open("A-small.out");
int t,kount,kt,k,s,ans,n,count;
cin>>t;
kount=1;
while(t--){

cin>>n;
count=1;
if(n==0){
cout<<"Case #"<<kount<<": INSOMNIA"<<endl;
kount=kount+1;
}
else{
vector<int> arr(10,0);
kt=0;
while(1){
k=count*n;
while(k>0){
s=k%10;	
if(arr[s]==0){
kt=kt+1;
arr[s]=1;	
}
k=k/10;

}
if(kt==10){
ans=count*n;
break;	
}

count=count+1;
}	
	
cout<<"Case #"<<kount<<": "<<ans<<endl;
kount=kount+1;

}

}	
	
	
	
	
	return 0;
}
