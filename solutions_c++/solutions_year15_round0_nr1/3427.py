#include <iostream>
#include <math.h>
#include <vector>
#include <stdlib.h>
#include <string>
#include <locale.h>
using namespace std;
__int64 ans[2000];
int main() {
	freopen("11.in","r",stdin);
	freopen("2.txt","w",stdout);
	int t,len;
	string s;
	cin>>t;
	for (int i=0;i<t;i++) {
	cin>>len;
	cin>>s;
	vector<int> arr;
	arr.clear();
	for (int i=0;i<=len;i++) arr.push_back(s[i]-'0');
	__int64 sum=0;
	//int dif=1;
	__int64 count=0;
	sum=arr[0];
	for (int i=1;i<=len;i++) {
	if (sum<i && arr[i]>0) 	{count+=(i-sum);sum+=(i-sum);}
	sum+=arr[i];
	
	}
	ans[i]=count;
	//cout<<sum<<endl;
	}
	for (int i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	return 0;
}


// 110011
// 012345 i
// 122256 sum 
// 000020 i-sum
// sum+=(i-sum)+arr[i];

