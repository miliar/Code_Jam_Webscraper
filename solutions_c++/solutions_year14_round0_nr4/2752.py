// teststl.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//source here
#include<iostream>
#include<map>
#include<string>
#include<fstream>
#include<iomanip>
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
void click() {
	int t;
	cin>>t;
	for (int cases=1; cases<=t; cases++) {
		double c,f,x;
		cin>>c>>f>>x;
		int m = x/f;
		double time = x/2;;
		double ftime = 0.0;
		double now = 2.0;
		ftime += c/now;
		now += f;
		while(time > ftime+x/now) {
			time = ftime+x/now;
			ftime += c/now;
			now += f;
		}
		cout<<"Case #"<<cases<<": "<<fixed<<setprecision(7)<<time<<endl;
	}

}

int cmp(const void *p1, const void *p2) {
	double a = *((double *)p1);
	double b = *((double *)p2);
	if (a<b) return 1;
	if (a>b) return -1;
	return 0;
}
void Dec() {
	int t;
	cin>>t;
	double now[1001];
	double ken[1001];
	for (int cases=1; cases<=t; cases++) {
		int n;
		cin>>n;
		for (int i=0; i<n; i++) cin>>now[i];
		for (int i=0; i<n; i++) cin>>ken[i];
		qsort(now,n,sizeof(now[0]),cmp);
		qsort(ken,n,sizeof(ken[0]),cmp);
		int score1 = 0;
		//耍赖玩法
		int start = 0;
		int end = n-1;
		for (int i=0; i<n; i++) {
			if ( now[start] > ken[i] ) {
				//如果这个数能大过 就大他 不然就让最小的上
				++score1;
				++start;
			} else {
				--end;
			}
		}
		int score2 = 0;
		//老实人玩法
		start = 0;
		end = n-1;
		for (int i=0; i<n; i++) {
			if ( ken[start] > now[i] ) {
				//如果这个数能大过 就大他 不然就让最小的上
				++start;
			} else {
				--end;
				++score2;
			}
		}
		cout<<"Case #"<<cases<<": "<<score1<<" "<<score2<<endl;
	}

}
int main() {
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
//    MagicTrick();
	//click();
	Dec();
	fclose(stdin);
	fclose(stdout);
    return 0;
}
