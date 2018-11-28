#include "iostream"
#include "stdio.h"
#include "cmath"
#include "cstring"
using namespace std;

#define pi 	3.14159265359
#define e 	2.71828

#define FOR(max) for(int i=0;i<max;i++)
#define FORi(i,max) for(int i=0;i<max;i++)
#define FOR2(min,max) for(int i=min;i<=max;i++)
#define FOR2i(i,min,max) for(int i=min;i<=max;i++)
#define SQR(n) ((n)*(n))
#define CUBE(n) ((n)*(n)*(n))



int main(){
	#ifdef CODEJAM_INPUT
		freopen("in.txt","r",stdin);
		freopen("A-small-practice.out","w",stdout);
	#endif

	int T,ans,ch1,ch2,exists;
	cin>>T;

	int **A= new int*[4];
	FOR(4){
		A[i]= new int[4];
	}

	int *row=new int[4];

	// cout<<T;
	// return 0;

	//T=2;
	FORi(tt,T){
		ans=-1;
		exists=0;

		cin>>ch1;
		FORi(i,4)
			FORi(j,4)
				cin>>A[i][j];
		
		FOR(4){
			row[i]=A[ch1-1][i];
		}

		cin>>ch1;
		FORi(i,4)
			FORi(j,4)
				cin>>A[i][j];

		exists=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(A[ch1-1][i]==row[j]){
					exists++;
					//cout<<row[j]<<endl;
					if(exists>1){
						goto here;
					}
					else{
						ans=row[j];
					}
				}
			}
		}
	here:

		//cout<<exists<<endl;
		printf("Case #%d: ",tt+1);
		if(exists==0){
			printf("Volunteer cheated!");
		}
		else if(exists==1){
			printf("%d",ans);
		}
		else{
			printf("Bad magician!");
		}
		cout<<endl;

		//printf("Case #%d: %d\n",tt+1,ans);
		
	}

	return 0;
}