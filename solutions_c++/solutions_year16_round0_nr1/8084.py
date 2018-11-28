#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(){
//    FILE *fin = freopen("A-small.in", "r", stdin);
//	assert( fin!=NULL );
//	FILE *fout = freopen("A-small.out", "w", stdout);

    ifstream fin;
	fin.open("A-large-attempt0.in");
    ofstream fout;
	fout.open("A-large.out");
int T,check,k,s,lastnum,n,count;
fin>>T;
//kount=1;
for(int t=1;t<=T;t++){

fin>>n;
count=1;
if(n==0){
fout<<"Case #"<<t<<": INSOMNIA"<<endl;
//kount=kount+1;
}
else{
vector<int> arr(10,0);
check=0;
while(1){
k=count*n;
while(k>0){
s=k%10;	
if(arr[s]==0){
check=check+1;
arr[s]=1;	
}
k=k/10;

}
if(check==10){
lastnum=count*n;
break;	
}

count=count+1;
}	
	
fout<<"Case #"<<t<<": "<<lastnum<<endl;
//kount=kount+1;

}

}	
	
	
	
	
	return 0;
}
