#include <bits/stdc++.h>
using namespace std;
int t;
int n;
int a[3][100];

void sort(){
	int i; 
	int j;
	for(i=0; i<n; i++){
		for(j=i; j<n; j++){
			if(a[1][i]<a[1][j]){
				swap(a[1][i],a[1][j]);
				swap(a[0][i],a[0][j]);
			}
		}
	}
}
void solve(int k){
	int i,j;
	cout<<"Case #"<<k<<": ";
	while(a[1][0]!=0){
		sort();
		

		if(a[1][0]-a[1][1]>1){
			if(a[1][0]==2 && a[1][1]==1&& a[1][2]==0){
				printf("%c ",'A'+a[0][0]);
				a[1][0]--;
			}
			else
			{
				printf("%c%c ",'A'+a[0][0],'A'+a[0][0]);
				a[1][0]-=2;
			}
		}
		else if(a[1][0]==1 && a[1][2]==1 && a[1][3]==0){
			printf("%c %c%c",'A'+a[0][2],'A'+a[0][0],'A'+a[0][1] );
			a[1][0]--;
			a[1][1]--;
			a[1][2]--;
		}
		else if(a[1][0]==2 && a[1][1]==1&& a[1][2]==0){
				printf("%c ",'A'+a[0][0]);
				a[1][0]--;
		}
		else if(a[1][0]==a[1][1]){
			printf("%c%c ",'A'+a[0][0],'A'+a[0][1]);
			a[1][0]--;
			a[1][1]--;
		}
		else if(a[1][0]>a[1][1]){
			printf("%c%c ",'A'+a[0][0],'A'+a[0][1]);	
			a[1][0]--;
			a[1][1]--;
		}

		else{
			printf("%c ",'A'+a[0][0]);
			a[1][0]--;
		}

	}
	cout<<endl;
	//debug
	//for(j=0; j<n; j++){
	//		printf("%c = %d\n",'A'+a[0][j],a[1][j]);	
	//	}
	//end debug
}

int main(int argc, char const *argv[])
{
	
	ifstream in("input.txt");
	in>>t;
	int i,j;

	for(i=1; i<=t; i++){
		in>>n;
		for(j=0; j<n; j++){
			a[0][j]=j;
			in>>a[1][j];
		}


		solve(i);
		// debug
		//for(j=0; j<n; j++){
			//printf("%c = %d\n",'A'+a[0][j],a[1][j]);	
		//}	
		//end debug
	}


	return 0;
}
