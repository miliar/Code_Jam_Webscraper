#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>
#include <math.h>

using namespace std;

int timesplus(int a, int b){
	if(a==1){
		if(b==1)
			return 	1;
		if(b==2)
			return 2;
		if(b==3)
			return 3;
		if(b==4)
			return 4;
	}
	if(a==2){
		if(b==1)
			return 2	;
		if(b==2)
			return -1;
		if(b==3)
			return 4;
		if(b==4)
			return -3;
	}
	if(a==3){
		if(b==1)
			return 	3;
		if(b==2)
			return -4;
		if(b==3)
			return -1;
		if(b==4)
			return 2;
	}
	if(a==4){
		if(b==1)
			return 	4;
		if(b==2)
			return 3;
		if(b==3)
			return -2;
		if(b==4)
			return -1;
	}
	while(1)
		cout<<"NAAAAAAAAAAAAAAAAAAA"<<endl;
	
}
int times(int a,int b){
	if(a>0 && b>0)
		return timesplus(a,b);
	if(a>0 && b<0)
		return -1*timesplus(a,-1*b);
	if(a<0 && b>0)
		return -1*timesplus(-1*a,b);
	else
			return timesplus(-1*a,-1*b);
			
		while(1)
		cout<<"NAAAAAAAAAAAAAAAAAAA"<<endl;
	
}

int secondoperator(int a, int res){
		for(int i=1;i<=4;i++)
			if(times(a,i)==res)
				return i;
		
		for(int i=1;i<=4;i++)
			if(times(a,-1*i)==res)
				return -1*i;
		
}
int cov(char c){
	if(c=='i')
		return 2;
	if(c=='j')
		return 3;
	else
		return 4;
}
int main(){
	ifstream in("in");
	int casenum=0;
	in>>casenum;
	int L,X,XC;
	int first[9];
	for(int c=0;c<casenum;c++){
		for(int i=0;i<9;i++)
			first[i]=-1;
		int A[10000];
		int B[10000];	
		in>>L>>X;
		XC=X;
		char ca;
		for (int i=0;i<L;i++){
			in>>ca;
			int l=cov(ca);
			B[i]=l;
			if(i==0)
				A[i]=l;
			else
				A[i]=times(A[i-1],l);
				
			if(first[A[i]+4]==-1)
				first[A[i]+4]=i;
		}
		
		int sofar=1;
		int currentind=0;
		int solution=2;
		while(X>0 && solution <=4){
			
			int searchfor=secondoperator(sofar,solution);
			//cout<<"searchfor:"<<sofar<<" "<<solution<<" "<<searchfor<<endl;
			//cout<<currentind<<endl;
			if(currentind==0){
				if(first[searchfor+4]!=-1){
					currentind=first[searchfor+4]+1;
					sofar=1;
					solution++;
				}
				else{
					X--;
					sofar=times(sofar,A[L-1]);
				}
			}
			else{
				for(int ti=currentind;ti<L;ti++){
					sofar=times(sofar,B[ti]);
					currentind=ti+1;
					if(sofar==solution){
						solution++;
						//cout<<"solution++"<<endl;
						sofar=1;
					}
				}
				
			}
			if(currentind==L){
				currentind=0;
				X=X-1;
			}
		}
		if(solution==5){
			sofar=1;
				for(int i=0;i<XC;i++)
					sofar=times(sofar,A[L-1]);
				if(sofar==times(2,times(3,4)))
					cout<<"Case #"<<c+1<<": YES"<<endl;
				else
					cout<<"Case #"<<c+1<<": NO"<<endl;
				/*if(X==0)
					cout<<"Case #"<<c+1<<": YES"<<endl;
				else{
					sofar=1;
					while(X!=0){
						if(currentind!=0){
							for(int ti=currentind;ti<L;ti++){
								sofar=times(sofar,B[ti]);
							}
							X--;
							currentind=0;
						}
						else{
							sofar=times(sofar,A[L-1]);
							X--;
						}
				
					}
					if(sofar==1)
						cout<<"Case #"<<c+1<<": YES"<<endl;
					else
						cout<<"Case #"<<c+1<<": NO"<<endl;
				}*/
		}
		else
			cout<<"Case #"<<c+1<<": NO"<<endl;
		
	}
		//finding i;
	
	return 0;
	
}
