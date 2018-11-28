#include<bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int s;
	//int *arr;
	char c;
	string s1;
//	cout<<"The value of t :"<<t<<endl;
	int answer=0;
	int t1=0;
	while(t1<t){
		t1++;
		answer=0;
		cin>>s;
		//cin>>c;
		cin>>s1;
		//cout<<s1;
		//cout<<s<<endl;
		//arr = new int[s+1];
		//for(int i=0;i<s+1;i++){
		//	cin>>arr[i];
		//}
		//for(int i=0;i<s+1;i++){
		//	cout<<arr[i]<<", ";
		//}
		//cout<<endl;
		int sum=0;
		for(int i=0;i<s1.length()-1;i++){
			sum = sum+int(s1[i])-48;
			//cout<<sum;
			if(sum<i+1&&s1[i+1]!='0'){
				answer += (i+1)-sum;
				sum += (i+1)-sum;
			}
		}
		//cout<<endl;
		cout<<"Case #"<<t1<<": "<<answer<<endl;
	}
	return 0;
}
