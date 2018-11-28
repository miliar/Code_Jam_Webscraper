#include <iostream>
#include <cstdio>
using namespace std;
void test(int a[4][4],int b[4][4],int m, int n);

int main(){
	int count;
	FILE *fin,*fout;
	//fin=fopen("A-small-attempt0.in","rb");
	//fout=fopen("test.out","wb");
	freopen("A-small-attempt4.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>count;
	int (*data)[4][4]=new int[count*2][4][4];
	int *num = new int[2*count];
	for(int i=0;i<2*count;i++){
		cin>>num[i];
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		cin>>data[i][j][k];
	}
	for(int i=0;i<count;i++){
	cout<<"Case #"<<i+1<<": ";
	test(*(data+2*i),*(data+2*i+1),num[2*i],num[2*i+1]);
	}
	return 0;
}
void test(int a[4][4],int b[4][4],int m, int n){
	int temp;
	int total=0;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++){
	if(a[m-1][i]==b[n-1][j]){
       total+=1;
	   if(total==1)
	   temp=a[m-1][i];
	}
	}
   if(total==1)
   cout<<temp<<endl;
   else if(total>1)
   cout<<"Bad magician!"<<endl;
   else
   cout<<"Volunteer cheated!"<<endl;
}
