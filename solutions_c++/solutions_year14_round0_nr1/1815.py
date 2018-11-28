#include<iostream>
using namespace std;
#define N 4
void Fn(int row[],int &count,int &index);
int main(){
	int n,k,i,j,s,r,count,index,row[N+1];
	cin>>n;
	for(k=1;k<=n;k++){
		count=0;//初始化
		cin>>r;
		s=N*(r-1)+1;//保存从第j个开始的4个数
		for(i=1;i<=N*N;i++)
			if(i==s){
				for(j=1;j<=4;j++)
					cin>>row[j];
				i+=3;
			}
			else cin>>row[0];

		cin>>r;
		s=N*(r-1)+1;
		for(i=1;i<=N*N;i++)
			if(i==s){
				for(j=1;j<=4;j++){
					cin>>row[0];
					Fn(row,count,index);
				}
				i+=3;
			}
			else cin>>row[0];

		cout<<"Case #"<<k<<": ";

		if(count>1)
			cout<<"Bad magician!"<<endl;
		else if(count==1)
			cout<<row[index]<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}
}
void Fn(int row[],int &count,int &index){
	int i;
	for(i=1;i<=N;i++)
		if(row[0]==row[i]){
			count++;
			index=i;
		}
}