#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
typedef unsigned long long int ULL;
using namespace std;
int main()
{
	ofstream myfile;
 	myfile.open ("magic_ouput.txt");
	int t,hash_table[16],choose1,choose2,first[4][4],second[4][4],flag;
	cin>>t;
	for(int i=1;i<=t;++i){	
		flag = 0;	
		for(int j=0;j<=15;++j)
			hash_table[j] = 0;
			
		scanf("%d",&choose1);
		for(int j=0;j<=3;++j){
			for(int k=0;k<=3;++k)
				scanf("%d",&first[j][k]);
		}
		for(int l=0;l<=3;++l)
			hash_table[first[choose1-1][l]-1]++;
		
		scanf("%d",&choose2);
		for(int j=0;j<=3;++j){
			for(int k=0;k<=3;++k)
				scanf("%d",&second[j][k]);
		}
		int l,count=0,ans;
		for(l=0;l<=3;++l){
			if( hash_table[second[choose2-1][l]-1] == 1){
				count++;
				ans = second[choose2-1][l];
			}
		}
		if(count == 1)
			myfile<<"Case #"<<i<<":"<<" "<<ans<<endl;
		//	printf("Case #%d: %d\n",i,ans);
		else if(count == 0)
		//	printf("Case #%d: Volunteer cheated!\n",i);
			myfile<<"Case #"<<i<<":"<<" "<<"Volunteer cheated!"<<endl;
		else
		//	printf("Case #%d: Bad magician!\n",i);
			myfile<<"Case #"<<i<<":"<<" "<<"Bad magician!"<<endl;
	}
	return 0;
}


