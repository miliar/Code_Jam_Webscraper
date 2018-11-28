#include<bits/stdc++.h>
using namespace std;

int findMin(int *arr, int size, int time)
{
	bool flag=false;
	for(int i=0;i<size;i++){
		if(arr[i]>0)
			flag=true;
	}
	if(!flag)
		return time;
	int arr1[size], arr2[size+1];
	for(int i=0;i<size;i++)
		arr1[i]=arr[i]-1;
	int maxm=arr[0];
	for(int i=0;i<size;i++){
		maxm=max(maxm, arr[i]);
	}
	if(maxm==1 || maxm==2 || maxm==3)
		return time+maxm;
	flag=false;
	for(int i=0;i<size;i++){
		if(!flag && arr[i]==maxm){
			arr2[i]=maxm-maxm/2;
			flag=true;
		}
		else
			arr2[i]=arr[i];
	}
	arr2[size]=maxm/2;
	int arr3[size+1];
	if(maxm==9){
		flag=false;
		for(int i=0;i<size;i++){
			if(!flag && arr[i]==maxm){
				arr3[i]=6;
				flag=true;
			}
			else
				arr3[i]=arr[i];
		}
		arr3[size]=3;
	}
	if(maxm==9)
		return min(findMin(arr1, size, time+1), min(findMin(arr2, size+1, time+1), findMin(arr3, size+1, time+1)));
	else
		return min(findMin(arr1, size, time+1), findMin(arr2, size+1, time+1));
}

int main()
{
	freopen("V:\\vikky_codder\\input.txt", "r", stdin);
	freopen("V:\\vikky_codder\\output.txt", "w", stdout);
	int tc, d, arr[1010];;
	cin>>tc;
	for(int t=1;t<=tc;t++){
		scanf("%d", &d);
		for(int i=0;i<d;i++){
			scanf("%d", &arr[i]);
		}
		int ans=findMin(arr, d, 0);
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
