#include<bits/stdc++.h>
#define lli long long

using namespace std;

typedef struct{
	char p;
	int ct;
} party;

bool comp(party p1,party p2){
	return p1.ct > p2.ct;
}

int main(){
	
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	
	int t;
	cin>>t;
	for(int tt = 0 ; tt < t ; tt ++ ){
		int n;
		cin>>n;
		vector<party> arr(n+1);
		arr[n].ct = 0;
		int sum = 0;
		for(int i=0;i<n;i++)
		{
			cin>>arr[i].ct;
			sum+=arr[i].ct;
			arr[i].p = i + 65;
		}
		
		sort(arr.begin() , arr.end() , comp);
		cout<<"Case #"<<tt+1<<": ";
		
		while(sum > 0){
			if(sum%2 == 1){
				for(int i=n-1;i>=0;i--){
					if(arr[i].ct%2 == 1){
						cout<<arr[i].p<<" ";
						arr[i].ct--;
						sum--;
						break;
					}
				}
			}
			for(int i=0;i<n;i++){
				if(arr[i].ct == arr[i+1].ct && arr[i+1].ct == arr[i+2].ct)
				continue;
				else if(arr[i].ct == arr[i+1].ct && arr[i].ct > 0){
					cout<<arr[i].p<<arr[i+1].p<<" ";
					arr[i].ct--;
					arr[i+1].ct--;
					sum-=2;
					i++;
				}
				else if(arr[i].ct > arr[i+1].ct && arr[i].ct > 1){
					cout<<arr[i].p<<" "<<arr[i].p<<" ";
					arr[i].ct-=2;
					sum-=2;
				}
				if(arr[i].ct == 0 && arr[i-1].ct > arr[i].ct && arr[i].ct < arr[i+1].ct){
					swap(arr[i].ct,arr[i+1].ct);
					swap(arr[i].p,arr[i+1].p);
				}
			}
		}
		cout<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}
