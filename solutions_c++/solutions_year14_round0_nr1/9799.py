#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int a[5][5],anw[5],lines;
	int i,j,c,tmp,num=1;
	int t;
	cin >> t;
	while(t--){
		c=0;
		memset(anw,0,sizeof(anw));
		cin >> lines;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin >> a[i][j];
		for(i=1;i<=4;i++)
			anw[i]=a[lines][i];
			
		cin >> lines;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin >> a[i][j];
				
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if(a[lines][j]==anw[i]){
					c++;
					tmp=anw[i];
				}
		if(c==0)
			cout << "case #" << num << ": " << "Volunteer cheated!" <<endl;
		else if(c==1)
			cout << "case #" << num << ": " << tmp <<endl;
		else if(c>1)
			cout << "case #" << num << ": " << "Bad magician!"	 <<endl;
		num++;			
	}
	return 0;
}