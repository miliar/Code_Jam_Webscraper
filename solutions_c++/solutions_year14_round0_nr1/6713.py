#include<iostream>
#include<fstream>


using namespace std;

int main(){
	freopen("C:\\Users\\cychan442\\Desktop\\in.txt","r",stdin);
	freopen("C:\\Users\\cychan442\\Desktop\\out.txt","w",stdout);
	int N;
	cin>>N;
	for(int ii=1;ii<=N;ii++){
		int ans=0,card[2][6],dummy;
		for(int i=0;i<2;i++){
			int temp;
			cin>>temp;
			for(int j=1;j<=4;j++)
				for(int k=0;k<4;k++)
					if(j==temp)
						cin>>card[i][k];
					else
						cin>>dummy;
		}
		int count=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				if(card[0][i]==card[1][j]){
					count++;
					ans=card[0][i];
				}
		}
		cout<<"Case #"<<ii<<": ";
		if(count==0)cout<<"Volunteer cheated!";
		if(count>1)cout<<"Bad magician!";
		if(count==1)cout<<ans;
		cout<<endl;
	}
	//cin>>N;
}