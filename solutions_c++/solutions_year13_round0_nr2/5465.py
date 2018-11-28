#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

//int getAns(int lawn[][101],int n,int m){
//	int ans=1,r;
//	//Checking Rows
//	for(int i=0;i<n;i++){
//		r=lawn[i][0];
//		for(int j=1;j<m;j++){
//			if(lawn[i][j]>r)
//				//
//		}
//	}
//}

int main(){
	
	ifstream in("inp.in");
	ofstream out("A-small-attempt0.out");

	int test;
	char nxt[10];
	in>>test;
	in.getline(nxt,10);
	for(int z=0;z<test;z++){
		int lawn[101][101],n,m;
		//int ans=0;
		int flag1=1,flag2=1,flag=1;

		//INPUT THE VALUES
		in>>n;
		in>>m;
		//in.getline(nxt,10);

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				in>>lawn[i][j];
			}
		}

		//each num is tested?
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				flag=1;
				//if number is 1, then the whole column must be one!
				if(lawn[i][j]==1){
					flag1=1;
					flag2=1;

					for(int a=0;a<n;a++)
						if(lawn[a][j] != 1){
							flag1=0;
							break;		//not possible! Now check for the row next. if it isn't all 1, then ans is NO
						}
					for(int a=0;a<m;a++)
						if(lawn[i][a]!=1){
							flag2=0;
							break;
						}
						//FUCK WHY IS IT STILL NOT CORRECT
						if(!(flag1||flag2)){
							out<<"Case #";
							out<<z+1;
							out<<": NO\n";
							flag=0;
							break;
						}				//such a small prob... turned into so mig a headache! :/
				}
			}
			if(!flag)
				break;
		}
		if(flag){
			out<<"Case #";
			out<<z+1;
			out<<": YES\n";
		}


	}

	in.close();
	out.close();
	return 0;
}