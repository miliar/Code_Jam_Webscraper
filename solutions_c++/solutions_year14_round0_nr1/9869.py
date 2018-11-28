#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
	int cn,k;
	cin>>cn;
	for(k=1;k<=cn;k++){
	int row1,row2,cnt,i,x;
	bool done=false;
	vector<int> v1(4,0);
	vector<int> v2(4,0);

	cin>>row1;
	cnt=1;
	while(cnt <= 4){
		if(cnt == row1){
			for(i=0;i<4;i++)
				cin>>v1[i];
		}else
		for(i=0;i<4;i++)
			cin>>x;
		cnt++;
	}
	cin>>row2;
	cnt=1;
	while(cnt <= 4){
		if(cnt == row2){
			for(i=0;i<4;i++)
				cin>>v2[i];
		}else
		for(i=0;i<4;i++)
			cin>>x;
		cnt++;
	}

	//calculate answer
	int num,j,ans;
	num = 0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(v1[i] == v2[j]){
				num++;
				if(!done){
					ans = v1[i];
					done = true;
				}
			}
		}
	}
	//producing answer
	if(num == 0)
		cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
	if(num == 1)
		cout<<"Case #"<<k<<": "<<ans<<endl;
	if(num > 1)
		cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	}
	
}
