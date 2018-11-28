#include<iostream>
#include<fstream>
#include <iomanip>
#include<stdlib.h>
#include<string>
#include<algorithm>
#define cin fcin
#define cout fout
using namespace std;
ifstream fcin("date.in.txt");
ofstream fout("date.out.txt");
double  a[10005];
double  b[10005];
int used[10005];
int main(){
	int T;
	cin>>T;
	for(int w=1;w<=T;w++){
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		//int first=0;
		/*memset(used,0,sizeof(used));
		for(int k=0;k<n;k++){
			double key=a[k];
			int now=-1;
			for(int j=0;j<n;j++)
				if(b[j]>key&&!used[j])
					now=j;
				if(j!=-1){used[j]=1;first++;}
		}*/
		//memset(used,0,sizeof(used));
		sort(a,a+n);
		sort(b,b+n);
		int j=0;
		int sum=0;
		for( i=0;i<n;i++){
			while(a[j]<b[i]&&j<n)j++;
			if(j>=n)break;
			sum++;
			j++;
		}
        int first=0;j=0;
		for( i=0;i<n;i++){
			while(b[j]<a[i]&&j<n)j++;
			if(j>=n)break;
			first++;
			j++;
		}





		cout<<"Case #"<<w<<": "<<sum<<" "<<n-first<<endl;
	}
	return 0;
}