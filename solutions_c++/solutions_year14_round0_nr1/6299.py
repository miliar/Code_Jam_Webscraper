#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int t;
	std::ios_base::sync_with_stdio(false);
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	cin>>t;
	int k=0;
	while(k!=t){
		int First[4][4]={0};
		int Second[4][4]={0};
		int fval,sval;
		cin>>fval;
		for(int i=0;i<4;i++)
			cin>>First[i][0]>>First[i][1]>>First[i][2]>>First[i][3];
		cin>>sval;
		for(int i=0;i<4;i++)
			cin>>Second[i][0]>>Second[i][1]>>Second[i][2]>>Second[i][3];
		fval--;
		sval--;
		int count=0;
		int val=-1;
		for(int i=0;i<4;i++){
           for(int j=0;j<4;j++)
			if(First[fval][i]==Second[sval][j]){
				count++;
				val=First[fval][i];
			}
		}
		k++;
		//cout<<count<<endl;
		if(count>1)
			printf("Case #%d: Bad magician!\n",k);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else
			printf("Case #%d: %d\n",k,val);
	}

}
