#include<iostream>
#include<string>
#include<fstream>
using namespace std;

//const int NUM = 1001;
//bool stand[NUM] = {};
int main(){
	ofstream fcout("output.out");
	int T;
	cin>>T;
	int cases = 1;
	while(cases<=T){
		int smax;
		string aud;
		cin>>smax>>aud;
		int len = aud.length();
		//memset(stand, false, len+1);
		int cnt = 0;
		int res = 0;
		for(int i=0; i<len; i++){
			if(cnt>=i){//当前观众的可以加上去
				cnt += aud[i]-'0';
			}
			else{
				res += (i-cnt);
				cnt += (i-cnt);
				cnt += aud[i]-'0';
			}
		}
		//cout<<"Case #"<<cases<<": "<<res<<endl;
		fcout<<"Case #"<<cases<<": "<<res<<endl;
		cases++;
	}
	fcout.close();
	return 0;
}