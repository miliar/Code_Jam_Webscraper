#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int comp1[10],comp2[10];

int main(){
	

	int num1,num2,dirty;
	fstream myfile,myin;
	myfile.open("d:\\data.txt",ios::out);
	myin.open("d:\\A-small-attempt2.in",ios::_Nocreate);
	//if(!myfile)return;
	int T;
	myin>>T;

	for(int i=1; i<=T; i++){
		myin>>num1;
		for(int j=1; j<=4; j++){
			for(int k=1; k<=4; k++){
				if(j == num1) myin>>comp1[k];
				else myin>>dirty;
			}
		}
		myin>>num2;
		for(int j=1; j<=4; j++){
			for(int k=1; k<=4; k++){
				if(j == num2) myin>>comp2[k];
				else myin>>dirty;
			}
		}
		//比较一共有几个相同的数字
		int same = 0,res = -1;
		for(int j=1; j<=4; j++){
			for(int k=1; k<=4; k++){
				if(comp1[j] == comp2[k]){
					same += 1,res = comp1[j];
					break;
				}
			}
		}//for
		//输出结果
		if(!same) myfile<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else if(same == 1) myfile<<"Case #"<<i<<": "<<res<<endl;
		else myfile<<"Case #"<<i<<": Bad magician!"<<endl;
	}
	system("puase");
	return 0;
}