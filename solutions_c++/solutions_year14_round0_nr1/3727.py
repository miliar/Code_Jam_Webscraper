#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

int t;
cin>>t;
for(int p=0;p<t;p++){
	int t1,t2,temp;
	vector<int> arr(4);
	vector<int> arr2(4);

	cin>>t1;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) {
		if(i==t1-1) cin>>arr[j];
		else cin>>temp;
	}	

	cin>>t2;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) {
		if(i==t2-1) cin>>arr2[j];
		else cin>>temp;
	}

	int count=0,recorded=-1;
	sort(arr.begin(),arr.begin()+4);
	sort(arr2.begin(),arr2.begin()+4);
	int i=0,j=0;
	while(i<4&&j<4){
		if(arr[i]<arr2[j]) i++;
		else if(arr[i]>arr2[j]) j++;
		else {count++; recorded=arr[i];  i++;j++;}
	}
	if(count==0) cout<<"Case #"<<p+1<<": Volunteer cheated!"<<endl;
	else if(count==1) cout<<"Case #"<<p+1<<": "<<recorded<<endl;
	else cout<<"Case #"<<p+1<<": Bad magician!"<<endl;

}
}
