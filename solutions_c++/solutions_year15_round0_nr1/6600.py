#include<iostream>
#include<string>

using namespace std;

char arr[1001];

int countInvite(int level){
	int ans=0, claps=0;	//���x�H��
	for(int i=0; i<=level; i++){
		if(claps>=i) claps+=(arr[i]-48);
		else{
			if(arr[i]=='0') continue;	//�i��᭱��shylevel�S�[���A�N���ݭn�ܽ�
			ans+=(i-claps);
			claps+=(arr[i]-48+ans);
		}
	}
	return ans;
}

int main(){
	int cases,level;
	cin>>cases;
	for(int c=1; c<=cases; c++){
		cin>>level;
		cin.ignore(1,' ');
		cin.getline(arr,1000);
		cout<<"Case #"<<c<<": "<<countInvite(level)<<endl;
	}
	return 0;
}