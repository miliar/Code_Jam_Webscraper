/* ..abhishek kumar.. */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
#define SMALL
int main(){
	#ifdef LARGE
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
	int t,n1,n2,a[100][100],b[100][100],i,j,cnt,f,k,l,x=1;
	cin>>t;
	while(t--){
		cnt=0;
		cin>>n1;
		for(i=1;i<=4;i++){
			for(k=1;k<=4;k++)
			cin>>a[i][k];
		}
		cin>>n2;
		for(j=1;j<=4;j++){
			for(l=1;l<=4;l++)
			cin>>b[j][l];
		}
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(a[n1][i]==b[n2][j]){
					f = a[n1][i];
					cnt++;
				}
			}
		}
		if(cnt==1){
			cout<<"Case #"<<x++<<": "<<f<<endl;
		}
		else if(cnt>1){
			cout<<"Case #"<<x++<<": "<<"Bad magician!"<<endl;
		}
		else if(cnt==0){
			cout<<"Case #"<<x++<<":  "<<"Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
