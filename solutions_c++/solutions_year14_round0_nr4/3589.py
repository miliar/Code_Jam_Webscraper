#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

ifstream fin("a.txt");
ofstream fout("ans.txt");
float arr[10000],brr[10000];
void mergeA(int beg,int mid,int end){
	float left[10000];
	float right[10000];
	for(int i=beg;i<=mid;i++)
		left[i]=arr[i];
	for(int i=mid+1;i<=end;i++)
		right[i]=arr[i];
	int i=beg;
	int j=mid+1;
	int l=beg;
	while(i<=mid&&j<=end){
		if(left[i]<right[j]){
			arr[l]=left[i];
			i++;
		}
		else{
			arr[l]=right[j];
			j++;
		}
		l++;
	}
	while(i<=mid){
		arr[l]=left[i];
		i++;
		l++;
	}
	while(j<=end){
		arr[l]=right[j];
		j++;
		l++;
	}
}

void merge_sortA(int beg,int end){
	int mid=(beg+end)/2;
	if(beg<end){
		merge_sortA(beg,mid);
		merge_sortA(mid+1,end);
		mergeA(beg,mid,end);
	}
}
void mergeB(int beg,int mid,int end){
	float left[10000];
	float right[10000];
	for(int i=beg;i<=mid;i++)
		left[i]=brr[i];
	for(int i=mid+1;i<=end;i++)
		right[i]=brr[i];
	int i=beg;
	int j=mid+1;
	int l=beg;
	while(i<=mid&&j<=end){
		if(left[i]<right[j]){
			brr[l]=left[i];
			i++;
		}
		else{
			brr[l]=right[j];
			j++;
		}
		l++;
	}
	while(i<=mid){
		brr[l]=left[i];
		i++;
		l++;
	}
	while(j<=end){
		brr[l]=right[j];
		j++;
		l++;
	}
}

void merge_sortB(int beg,int end){
	int mid=(beg+end)/2;
	if(beg<end){
		merge_sortB(beg,mid);
		merge_sortB(mid+1,end);
		mergeB(beg,mid,end);
	}
}

void main(){
	int total,row,k=1,var=0,var2=0;
	float temp;
	int j;

	fin>>total;
	while(k<=total){
		var=0;
		var2=0;
		fin>>row;
		for(int i=0;i<row;i++){
			fin>>temp;
			arr[i]=temp;
		}
		for(int i=0;i<row;i++){
			fin>>temp;
			brr[i]=temp;
		}
		merge_sortA(0,row-1);
		merge_sortB(0,row-1);

		j=0;
		for(int i=0;i<=row-1;i++){
			if(arr[i]>brr[j]){
				var++;
				j++;
			}
		}
 		j=row-1;
		 for(int i=row-1;i>=0;i--){
			if(arr[i]>brr[j]){
				var2++;
			}
			else if(arr[i]<brr[j]){
				j=j-1;
			}
		}
		fout<<"Case #"<<k<<": "<<var<<" "<<var2<<"\n";
		k++;
	}
}

