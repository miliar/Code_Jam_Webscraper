#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

int main(void){

	freopen("A-large.in","r",stdin);
	freopen("al.out","w",stdout);
	int t;
	cin>>t;

	int arr[10000];

	for(int test=0;test<t;test++){
		
		int x,m;
		cin>>x>>m;

		int i,j;
		for(int i=0;i<x;i++){
			cin>>arr[i];
		}

		sort(arr,arr+x);

		int head = 0;
		int end = x-1;
		int counter = 0;
		while(end>=head){
			if(end==head){
				counter++;
				end--;
				head++;
			}
			else if(arr[end]+arr[head]<=m){
				head++;
				end--;
				counter++;
			}else{
				end--;
				counter++;
			}
		}
		printf("Case #%d: %d\n",test+1,counter);
	}
				
		



}