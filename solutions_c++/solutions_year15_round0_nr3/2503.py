#include <iostream>
#include <string>
using namespace std;
int arr1[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};


int func2(int mul,int flag , int x){
	if(x==0)return 1;
	int ret = 1;
	if(mul == 1){
		ret = 1;
	}
	if(x % 4== 0){
		if(mul == 2){
			ret =1;
		}
		else if(mul == 3){
			ret =1;
		}
		else if(mul == 4){
			ret =1;
		}
	}
	else if(x % 4== 1){
		if(mul == 2){
			ret =2;
		}
		else if(mul == 3){
			ret =3;
		}
		else if(mul == 4){
			ret =4;
		}
	}
	else if(x % 4== 2){
		if(mul == 2){
			ret =-1;
		}
		else if(mul == 3){
			ret =-1;
		}
		else if(mul == 4){
			ret =-1;
		}
	}
	else if(x % 4== 3){
		if(mul == 2){
			ret =-2;
		}
		else if(mul == 3){
			ret =-3;
		}
		else if(mul == 4){
			ret =-4;
		}
	}
	if(x % 2==0){
		flag*=flag;
	}
	return ret*flag;
}

bool func1(const string& s,int x){
	//i�� �O�´�.
	int index = -1;
	//���
	int flag = 1;
	//���� ����.
	int now = 1;
	string s1;
	while(true){
		index++;
		//��ã�� ������.
		if(index == s.size() && x== 0){
			return false;
		}
		if(index == s.size()){
			x--;
			index = 0;
		}
		now = arr1[now][(s[index]-'g')];
		//������
		if(now<0){
			flag *= -1;
			now *= -1;
		}
		//s1.push_back(s[index]);
		//i�� ã�Ҿ�
		if(now == 2){
			
			break;
		}
	}
	//cout<< s1<<endl;
	now = 1;
	//cout<< flag <<endl;
	string s2;
	while(true){
		index++;
		//��ã���� false;
		if(index == s.size() && x== 0){
			return false;
		}
		if(index == s.size()){
			x--;
			index = 0;
		}
		
		now = arr1[now][(s[index]-'g')];
		//������
		if(now<0){
			flag *= -1;
			now *= -1;
		}
		//s2.push_back(s[index]);
		//j�� ã�Ҿ�
		if(now == 3){
			break;
		}
	}
	
	//cout<<s2<<endl;
	now = 1;
	//cout<< flag <<endl;
	string s3;

	while(true){
		index++;
		
		//��ã���� false;
		if(index == s.size() && x== 0){
			return false;
		}
		if(index == s.size()){
			x--;
			index = 0;
		}
		
		now = arr1[now][(s[index]-'g')];
		//������
		if(now<0){
			flag *= -1;
			now *= -1;
		}
		//s3.push_back(s[index]);
		//k�� ã�Ҿ�
		if(now == 4){
			break;
		}
	}
	//cout<< s3<<endl;
	//cout<< flag <<endl;
	if(index == s.size()-1 && x== 0){
		if(flag == 1){
			return true;
		}
		return false;
	}

	//������
	int mul = 1;
	for(int i = index+1 ; i< s.size();i++){
		mul = arr1[mul][s[i]-'g'];
		if(mul < 0){
			mul *= -1;
			flag *= -1;
		}
	}
	
	//�ѹ��� �������� ������ ��
	int mul2 = 1;
	int flag2 = 1;
	for(int i = 0 ; i< s.size();i++){
		mul2 = arr1[mul2][s[i]-'g'];
		if(mul2 < 0){
			mul2 *= -1;
			flag2 *= -1;
		}
	}
	//���� x������ ����Ѵ�.
	int ret = func2(mul2 , flag2 , x);
	
	if(ret<0){
		ret*= -1;
		flag *= -1;
	}
	//cout<<mul<<" "<<ret;
	ret = arr1[mul][ret];
	return (ret * flag) == 1;
	
}

int main(){


	int t;
	cin >> t;
	int k = 1;
	while(t--){
		int L;
		int X;
		cin >> L;
		cin >> X;
		string s;
		cin >> s;
		
		cout<< "Case #"<<k<<": "<<(func1(s,X-1)? "YES" :"NO") <<endl;
		k++;
	}
	return 0;
}