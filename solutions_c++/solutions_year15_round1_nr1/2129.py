#include<iostream>

/**********
if(arr[i]-arr[i+1]>=0){
	if(arr[i]-arr[i+1]>=10) ans+=arr[i]-arr[i+1];
	else{ //0~9
		if(arr[i]<=10) ans+=arr[i];
		else ans+=10;
	}
}
else if(arr[i]-arr[i+1]<0){
	if(arr[i]<=10) ans+=arr[i];
	else ans+=10;
}
*********/

using namespace std;

int A1(int N, int arr[2000]){
	int ans=0;
	for(int i=0; i<N-1; i++){
		if(arr[i]-arr[i+1]>0) ans+=arr[i]-arr[i+1];
		else continue;
	}
	return ans;
}

int A2(int N, int arr[2000]){
	int ans=0, eatRate=0;
	for(int i=0; i<N-1; i++){
		if(arr[i]-arr[i+1]>0) eatRate=eatRate>(arr[i]-arr[i+1]) ? eatRate : arr[i]-arr[i+1];
	}
	for(int i=0; i<N-1; i++){
		if(arr[i]>=eatRate) ans+=eatRate;
		else ans+=arr[i];
	}
	return ans;
}

int main(){
	int cases,N,arr[2000];
	int ansA1,ansA2;
	cin>>cases;
	for(int c=1; c<=cases; c++){
		cin>>N;
		for(int i=0; i<N; i++) cin>>arr[i];
		ansA1=A1(N,arr);
		ansA2=A2(N,arr);
		cout<<"Case #"<<c<<": "<<ansA1<<" "<<ansA2<<endl;
	}
	return 0;
}