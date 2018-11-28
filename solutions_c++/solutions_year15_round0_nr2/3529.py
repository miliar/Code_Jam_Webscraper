#include <bits/stdc++.h>
using namespace std;
int time_to_divide(int a,int b){
	if(a<=b){
		return 0;
	}else{
		return 1+time_to_divide(a-b,b);
	}
}
int arr[1000];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int T;
	cin>>T;
	for(int x=0;x<T;x++){
		int D;
		cin>>D;
		for (int i=0;i<D;i++){
			cin>>arr[i];
		}
		int max = arr[0];
		for (int i=0;i<D;i++){
			if(arr[i]>max){
				max = arr[i];
			}
		}
		int min_time = 1001;
		for(int j=1;j<=max;j++){
			int total_time = 0;
			for(int i=0;i<D;i++){
				total_time+=time_to_divide(arr[i],j);
			}
			total_time+=j;
			if(total_time<min_time){
				min_time = total_time;
			}
		}
		cout<<"Case #"<<(x+1)<<": "<<min_time<<endl;
	}
	return 0;
}
