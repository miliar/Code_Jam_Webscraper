#include<iostream>
#include<string>
using namespace std;
int main(){
	int T,first,second,tmp;
	int tmp1[4], tmp2[4];
	cin >> T;
	
	for(int i=0;i<T;i++){
		cin >> first;
		//cout << "first = "<<first<<endl;
		for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				cin >> tmp;
				if(first == r+1){
					tmp1[c] = tmp;
				}
			}
		}
		cin >> second;	
		//cout << "second = "<<second<<endl;
		for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				cin >> tmp;
				if(second == r+1){
					tmp2[c] = tmp;
				}
			}
		}
		int flag = 0;
		int magic_num = -1;
		for(int a=0;a<4;a++){
			for(int b=0;b<4;b++){
				if(tmp1[a]==tmp2[b]){
					flag++;
					magic_num = tmp1[a];
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(flag == 0)
			cout << "Volunteer cheated!\n";
		else if(flag > 1)
			cout << "Bad magician!\n";
		else
			cout << magic_num << endl;

	}
	return 0;
}
