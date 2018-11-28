#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<algorithm>

using namespace std;
int search(float arr[],float p,int l,int r){
	if(p<arr[l])
	return l;
	else if(p>arr[r])
	return r+1;
	while(r>=l){
		int mid=(l+r)/2;
	if(p==arr[mid])
	return mid;
	else if(p>arr[mid])
	l=mid+1;
	else
	r=mid-1;

	}
	return l;
}


int main(){
int t,l=1;
cin>>t;

while(t--){
int n,ans1,ans2;
cin>>n;
float x,y;
float a[n],b[n];
bool a1[n],b1[n];

for(int i=0;i<n;i++){
	cin>>x;
	a[i]=(x*100000);
	a1[i]=0;
	b1[i]=0;
}

for(int i=0;i<n;i++){
	cin>>x;
	b[i]=(x*100000);
}
sort(a,a+n);
sort(b,b+n);
//for(int i=0;i<n;i++)
//cout<<a[i]<<" ";

//cout<<endl;

//for(int i=0;i<n;i++)
//cout<<b[i]<<" ";

//cout<<endl;


int v;
for(int i=0;i<n;i++){
v=search(b,a[i],0,n-1);
if(v!=n){
	for(int k=v;k<n;k++){
		if(a1[k]==1)
		v++;
		else{
			a1[k]=1;
			break;
		}
	}
}
if(v==n-1){
ans1=n-(i+1);
break;
}
if(v==n){
ans1=n-i;
break;
}
}
for(int i=0;i<n;i++){
v=search(a,b[i],0,n-1);
if(v!=n){
	for(int k=v;k<n;k++){
		if(b1[k]==1)
		v++;
		else{
			b1[k]=1;
			break;
		}
	}
}
if(v==n-1){
ans2=(i+1);
break;
}
if(v==n){
ans2=i;
break;
}
}


cout<<"Case #"<<l<<": "<<ans2<<" "<<ans1<<endl;
l++;
}

system("pause");
  return 0;
}
