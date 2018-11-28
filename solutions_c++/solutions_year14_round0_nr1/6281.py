#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<set>
#include<stack>
#include<vector>
#include<map>
#define fr(i) for(int i=1;i<=4;i++)
using namespace std;
#define MOD 1000000007
#define MAX 100
int main(){
	  int A[5][5];
		int B[5][5];
		int match=0;
		int val=0;
		int t;
		int r1,r2; 
		int v=0;
		cin >> t;
		while(t--){
			  v++;
				match=0;
		    cin >> r1;
				fr(i) fr(j)
					cin >> A[i][j];
		    cin >> r2;
				fr(i) fr(j)
					cin >> B[i][j];

				fr(i)
					fr(j){
					   if(A[r1][i] == B[r2][j]){
						    match++;
								val = A[r1][i];
						 }
					}

				if(match == 0){
				  cout << "Case #" << v << ": Volunteer cheated!\n";
				}else if(match==1){
				  cout << "Case #" << v << ": " << val << endl;
				}else{
				  cout << "Case #" << v << ": Bad magician!\n";
				}
					  
		}
    return 0;
}
