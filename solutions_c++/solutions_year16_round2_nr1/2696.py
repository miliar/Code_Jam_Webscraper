#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include <fstream>

using namespace std;

int main(){

	//FILE *read=fopen("C.in","r");
	//FILE *write=fopen("C_answer.txt","w");

	ifstream read;
	read.open("A.in");

	ofstream write;
	write.open("A_answer.txt");

	int t;
	//fscanf(read,"%d",&t);
	read>>t;

	string digit[10]={"ZERO","EIGHT","TWO","SIX","SEVEN","FIVE","FOUR","THREE","ONE","NINE"};

	vector<int> answer;

	for(int i=0;i<t;i++){
		string s;
		read>>s;


		write<<"Case #"<<i+1<<": ";

		for(int j=0;j<10;j++){
			bool found=true;
			for(int k=0;k<digit[j].length();k++){
				int find=s.find(digit[j][k]);

				if(j==4 && k==3 && find!=-1){
					string cop=s;
					cop.erase(find,1);
					find=cop.find(digit[j][k]);
				}else if(j==7 && k==4 && find!=-1){
					string cop=s;
					cop.erase(find,1);
					find=cop.find(digit[j][k]);
				}else if(j==9 && k==2 && find!=-1){
					string cop=s;
					cop.erase(find,1);
					find=cop.find(digit[j][k]);
				}
				
				if(find==-1){
					found=false;
					break;
				}
			}

			if(found){
				
				for(int k=0;k<digit[j].length();k++){
					int find=s.find(digit[j][k]);

					s.erase(find,1);
				}
				int val=j;
				if(val==1)val=8;
				else if(val==3)val=6;
				else if(val==4)val=7;
				else if(val==6)val=4;
				else if(val==7)val=3;
				else if(val==8)val=1;
				answer.push_back(val);
				j--;				

			}

		}

		sort(answer.begin(),answer.end());
		for(int j=0;j<answer.size();j++)write<<answer[j];
		answer.clear();
		write<<endl;
	}

	

	//fclose(read);
	//fclose(write);

	read.close();
	write.close();

	return 0;
}