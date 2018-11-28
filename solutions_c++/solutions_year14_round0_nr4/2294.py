#include<iostream>
#include<algorithm>
using namespace std;
double A[1010],B[1010];
int getBPoint(double A[1010],double B[1010],int num){
	int i,j=1,point=0;
	for(i=1;i<=num;i++){
		for(;j<=num;j++){
			if(B[j]>A[i]){
				point++;
				j++;
				break;
			}
		}
	}
	return point;
}
int getAPoint(double A[1010],double B[1010],int num){
	int istart=1,jstart=1,iend=num,jend=num,point=0;
	while(istart<=iend&&jstart<=jend){
		if(A[istart]<B[jstart]){
			jend--;
			istart++;
			point++;
		}else{
			istart++;
			jstart++;
		}
	}
	return point;
}
void show(double A[1010],int num){
	for(int i=1;i<=num;i++)
		cout<<A[i]<<" ";
	cout<<endl;
	return ;
}
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		int num;
		cin>>num;
		for(int j=1;j<=num;j++)
			cin>>A[j];
		for(int j=1;j<=num;j++)
			cin>>B[j];
		sort(A+1,A+num+1);
		sort(B+1,B+num+1);
		int truPoint = num-getAPoint(A,B,num);
		int falPoint = num-getBPoint(A,B,num);
		cout<<"Case #"<<i<<": "<<truPoint<<' '<<falPoint<<endl;
	}
return 0;
}