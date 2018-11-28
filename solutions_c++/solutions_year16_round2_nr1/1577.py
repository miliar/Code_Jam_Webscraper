#include<iostream>
#include<deque>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
int main (){
	ifstream cin("Alarge.in");
	ofstream cout("AE.txt");
	int count[26]={0};
	int x;
	cin>>x;
	string str;
	int output[10];
	for(int i=1;i<=x;i++){
		for(int j=0;j<26;j++){
			count[j]=0;
		}
		for(int j=0;j<10;j++){
			output[j]=0;
		}
		cin>>str;
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<str.size();j++){
			count[(int)str[j]-65]++;
		}
		//execute shit
		while(count[25]!=0){
			count[25]--;
			count[4]--;
			count[17]--;
			count[14]--;
			output[0]++;
		}while(count[22]!=0){
			count[22]--;
			count[19]--;
			count[14]--;
			output[2]++;
		}while(count[6]!=0){
			output[8]++;
			count[6]--;
			count[4]--;
			count[8]--;
			count[7]--;
			count[19]--;
		//	output[8]++;
		}while(count[20]!=0){
			output[4]++;
			count[5]--;
			count[14]--;
			count[20]--;
			count[17]--;
		}while(count[5]!=0){
			output[5]++;
			count[5]--;
			count[8]--;
			count[21]--;
			count[4]--;
		}
		while(count[23]!=0){
			output[6]++;
			count[18]--;
			count[8]--;
			count[23]--;
		}
		while(count[21]!=0){
			output[7]++;
			count[18]--;
			count[4]-=2;
			count[21]--;
			count[13]--;
		}while(count[8]!=0){
			output[9]++;
		//	cout<<count[8];
			count[13]-=2;
			count[8]--;
			count[4]--;
		}while(count[19]!=0){
			count[19]--;
			output[3]++;
			count[7]--;
			count[17]--;
			count[4]-=2;
		}while(count[13]!=0){
		//	cout<<count[13]<<endl;
		//	cout<<"one";
		//	count[13]--;
		//	count[]
		count[13]--;
		count[14]--;
		count[4]--;
			output[1]++;
		}
		for(int j=0;j<26;j++){
			if(count[j]!=0){
				cout<<"check next fgffffffffffffffffffffffffffffffffffff"<<endl;
			}
		}
		for(int j=0;j<10;j++){
			while(output[j]!=0){
				cout<<j;
				output[j]--;
			}
		}cout<<endl;
	}
}
