#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

//PS=>P
//RS=>R
//PR=>P

struct ee{
	string st;
	int p,s,r;
};
ee initial;
string ans;

string cal_min(string start, int m) {
	if (m==1)
	return start;
	string left="",right="";
	for (int i=0;i<m/2;i++) {
		left+=start[i];
		right+=start[i+m/2];
	}
	left=cal_min(left,m/2);
	right=cal_min(right,m/2);
	if (left<right)
	return left+right;
	else return right+left;
}

string cal(ee start, int m) {
	if (m>1 && (start.p+start.s<start.r || start.p+start.r<start.s || start.r+start.s<start.p))
	return "";
	if (m==1) {
		if (start.p==1)
		return "P";
		else if (start.s==1)
		return "S";
		else start.st="R";
		return "R";
	}
	ee temp;
	string a;
	temp.p=m/2-start.s;
	temp.s=m/2-start.r;
	temp.r=m/2-start.p;
	a=cal(temp,m/2);
	if (a!="") {
		string b="";
		for (int i=0;i<a.length();i++)
		if (a[i]=='P')
		b+="PR";
		else if (a[i]=='S')
		b+="PS";
		else b+="RS";
		a=b;
	}
	return a;
}

int main() {
	int T,t,n;
	cin>>T;
	for (t=1;t<=T;t++) {
		cin>>n>>initial.r>>initial.p>>initial.s;
		ans=cal(initial,1<<n);
		if (ans=="")
		printf("Case #%d: IMPOSSIBLE\n",t);
		else cout<<"Case #"<<t<<": "<<cal_min(ans,1<<n)<<endl;
	}
    return 0;
}
