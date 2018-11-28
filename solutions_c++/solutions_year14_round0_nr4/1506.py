#include <iostream>
#include<cmath>
#include<iomanip>
#include <fstream>
using namespace std;
int mi[31]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432};
int divide(double a[],int low,int high){
	double k=a[low];
	do {while (low<high&&a[high]>=k)--high;
	if(low<high){a[low]=a[high];++low;}
	while (low<high&&a[low]<=k)++low;
	if(low<high){a[high]=a[low];--high;}
	}while (low!=high);
	a[low]=k;
	return low;
}
void quicksort(double a[],int s,int e){
	if(s>=e)return ;
	int mid=divide(a,s,e);
	quicksort(a,s,mid-1);
	quicksort(a,mid+1,e);
}

int main(void) {
	ifstream cin("D-large.in");
    ofstream cout("humble.out");
    int k;
    cin>>k;
	for(int round=0;round<k;++round){
		int n;
		double maoni[1000], ken[1000];
		cin>>n;
		for(int i=0;i<n;++i)cin>>maoni[i];
		for(int i=0;i<n;++i) cin>>ken[i];
		quicksort(maoni,0,n-1);
		quicksort(ken,0,n-1);
		int cheat=0,notcheat=n;
		int m=0,k=0;
		while(k<n){
			if(maoni[m]<ken[k]){--notcheat; ++m;++k;}
			else ++k;
		}
		m=0;k=0;
		while(m<n){
			if(maoni[m]>ken[k]){++cheat; ++m;++k;}
			else ++m;
		}
		cout<<"Case #"<<round+1 <<": "<<cheat<<" "<<notcheat<<endl;
    }
	return 0;
}
