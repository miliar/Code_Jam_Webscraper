#include <iostream>
#include <vector>
using namespace std;

#define pb push_back

int main(){
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++){
		string s;
		cin>>s;
		/*vector<char> arr;
		arr.pb(s[0]);
		int n=s.size();
		for(int i=1;i<n;i++){
			if(s[i]<arr[0]){
				arr.pb(s[i]);
			}
			else{
				vector<char> newarr(arr.size()+1);
				newarr[0]=s[i];
				for(int j=0;j<arr.size();j++){
					newarr[j+1]=arr[j];
				}
				arr=newarr;
			}
		}*/
		int n=s.size();
		vector<char> arr(10*n);
		arr[5*n]=s[0];
		int lo=5*n-1,hi=5*n+1;
		for(int i=1;i<n;i++){
			if(s[i]<arr[lo+1]){
				arr[hi]=s[i];
				hi++;
			}
			else{
				arr[lo]=s[i];
				lo--;
			}
		}
		cout<<"Case #"<<te<<": ";
		for(int i=lo+1;i<hi;i++){
			cout<<arr[i];
		}
		cout<<endl;
	}
	return 0;
}