#include<bits/stdc++.h>
using namespace std;

int a[10];
//int dp[10][7];

int solve(int maxIndex, int* a, int t){
    if(maxIndex==1) return t+1;
    //if(dp[maxIndex][a[maxIndex]]!=-1) return dp[maxIndex][a[maxIndex]];
    int res=maxIndex+t;
    int acopy[10];
    t++;
    for(int i=1;i<=maxIndex/2;i++){

        for(int j=1;j<=9;j++){
            acopy[j]=a[j];
        }
        acopy[maxIndex]--;
        acopy[i]++;
        acopy[maxIndex-i]++;
        int maxIndexCopy=-1;
        for(int j=9;j>0;j--){
            if(acopy[j]!=0){
                maxIndexCopy=j;
                break;
            }
        }
        int temp;
        res=min(solve(maxIndexCopy,acopy,t),res);
    }
    return res;
}

int main(){
    int tc;

	cin>>tc;
	ofstream fout;
	fout.open("two.out");
	for(int z=1;z<=tc;z++){
         bool all9=true;
        //memset(dp,-1,sizeof(dp));
		int d, temp;
		cin>>d;
		memset(a,0,sizeof(a));
		for(int i=0;i<d;i++){
			cin>>temp;
			if(temp!=9) all9=false;
			a[temp]++;
		}
		int maxIndex=-1;
		for(int j=9;j>0;j--){
            if(a[j]!=0){
                maxIndex=j;
                break;
            }
        }
        if(all9 && d>=4)
            fout<<"Case #"<<z<<": "<<9<<endl;
        else fout<<"Case #"<<z<<": "<<solve(maxIndex,a,0)<<endl;
        //else  fout<<"Case #"<<z<<": "<<9<<endl;
	}
	fout.close();
}
