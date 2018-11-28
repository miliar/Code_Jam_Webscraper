// teststl.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//source here
#include<iostream>
#include<map>
#include<string>
#include<fstream>
using namespace std;
void ReadPhoneNumber() {
	int testC;
    cin>>testC;
	char p[101];
	char f[201];
	char res[1000];
	char number[10][20] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
	char map[11][20] = {"","","double","triple","quadruple","quintuple","sextuple","septuple","octuple","nonuple","decuple"};
    for (int test=1; test<=testC; test++) {
        memset(p,0,sizeof(p));
		memset(f,0,sizeof(f));
		memset(res,0,sizeof(res));
		cin>>p>>f;
		int pos = 0;
		int flen = strlen(f);
		int next = 0;
		int num = 0;
		int resIndex = 0;
		while (next <= flen ) {
			if (next == flen || f[next] =='-') {
				//从pos 开始的num个放在一起考虑
				int now = pos;
				int index = 1;
				int count = 1;
				while (index <=num) {
					if (index == num || p[pos+index] != p[now]) {
						//两种情况 增加字符串
						if (count == 1 || count > 10) {
							//挨个输出即可
							for (int k=0; k<count;k++) {
								int s = strlen(number[p[now]-'0']);
								res[resIndex++] = ' ';
								for (int l=0; l<s; l++) {
									res[resIndex++] = number[p[now]-'0'][l];
								}
							}
						} else {
							//直接接续在后面
							res[resIndex++] = ' ';
							for (int k=0; k<strlen(map[count]); k++) res[resIndex++] = map[count][k];
							res[resIndex++] = ' ';
							for (int k=0; k<strlen(number[p[now]-'0']);k++) res[resIndex++] = number[p[now]-'0'][k]; 
						}
						now = pos+index;
						++index;
						count = 1;
					} else {
						++count;
						++index;
					}
				}
				pos += num;
				num = 0;
			} else {
				num *= 10;
				num += f[next]-'0';
			}
			next++;
		}
		res[resIndex] = 0;
        cout<<"Case #"<<test<<":"<<res<<endl;
    }
};
void MagicTrick(){
	int t;
	cin>>t;
	int f[5][5];
	int s[5][5];
	for (int cases=1; cases<=t; cases++) {
		int a;
		cin>>a;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++)
				cin>>f[i][j];
		int b;
		cin>>b;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++)
				cin>>s[i][j];
		int count = 0;
		int val;
		for (int j=1; j<=4; j++)
			for (int k=1;k<=4;k++)
				if (f[a][j] == s[b][k]){
					count++;
					val = f[a][j];
				}
		cout<<"Case #"<<cases<<": ";
		if (count==0) cout<<"Volunteer cheated!"<<endl;
		else if (count == 1) cout<<val<<endl;
		else cout<<"Bad magician!"<<endl;
	}
};

int main() {
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
    MagicTrick();
	fclose(stdin);
	fclose(stdout);
    return 0;
}
