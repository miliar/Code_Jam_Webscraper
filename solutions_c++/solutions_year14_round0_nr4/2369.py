#include<iostream>
#include<string>
#include<conio.h>
#include<vector>
#include<map>
using namespace std;
int divide(float arr[], int beg, int end)          
{
	int p=beg, loc;
	float pivot=arr[beg];
	for(loc=beg+1;loc<=end;loc++)
	{
		if(pivot<arr[loc])
		{
			arr[p]=arr[loc]; 		arr[loc]=arr[p+1]; 		arr[p+1]=pivot;
			p=p+1;
		}
	}
	return p;
}

void QuickSort(float arr[], int beg, int end)
{
	if(beg<end)
	{
		int p=divide(arr,beg,end);                       

		QuickSort(arr,beg,p-1);                             
		QuickSort(arr,p+1,end);			              
	}
}

int main(void){
	//freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("largeOutputD.txt", "w", stdout);
	//freopen("smallOutputD.txt", "w", stdout);
	int T; cin>>T;
	for(int tc=1;tc<=T;tc++){
		cout<<"Case #"<<tc<<": ";
		float wts1[1000] = {0,}; float wts2[1000] = {0,};
		int N ;cin>>N;
		for(int i=0;i<N;i++){
			cin>>wts1[i];
		}
		for(int i=0;i<N;i++){
			cin>>wts2[i];
		}
		QuickSort(wts1,0,N-1);
		QuickSort(wts2,0,N-1);
		int count =0;
		for(int i=0,p=0;i<N;i++){
			if(wts1[p]  > wts2[i]){
				count++; p++;
			}
		}
		cout<<count<<' '; 
		count=0;
		for(int i=0,p=0;i<N;i++){
			if(wts2[p]  > wts1[i]){
				count++; p++;
			}
		}
		cout<<N - count;
		cout<<'\n';
	}
	fclose(stdin); fclose(stdout);
}