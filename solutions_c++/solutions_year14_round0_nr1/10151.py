#include <iostream>
#include <cstring>
#include <stdio.h>

using namespace std;

int T;
int num[17];
int mag[5][5];
int row;

int main(){
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	int tu = 0;
	while(T--){
		tu++;
		memset(num,0,sizeof(num));
		for(int ti = 1; ti <= 2; ti++){
			cin>>row;
			int i,j;
			for(i = 1; i <= 4; i++){
				for(j = 1; j <= 4; j++){
					cin>>mag[i][j];
				}
			}
			for(i = 1; i <= 4; i++){
				num[mag[row][i]]++;
			}
		}
		int count1 = 0;
		int index;
		for(int i = 1; i <= 16; i++){
			if (num[i] >= 2){
				count1++;
				index = i;	
			}
		}
		if (count1 == 1)
			cout<<"Case #"<<tu<<": "<<index<<endl;
		if (count1 > 1)
			cout<<"Case #"<<tu<<": "<<"Bad magician!"<<endl;
		if (count1 < 1)
			cout<<"Case #"<<tu<<": "<<"Volunteer cheated!"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
