#include <iostream> 
using namespace std;

int solve(int matrix1[][4],int matrix2[][4], int x1,int x2,int *num) {
     char used[16]={0};
     int count = 0;
     for(int i=0;i<4;++i) {
	used[matrix1[x1-1][i]] = 1;
     }
     for(int i=0;i<4;++i) {
     	if(used[matrix2[x2-1][i]] == 1) {
	    count ++;
	    *num = matrix2[x2-1][i];
	}
     }
    return count;	
}
int main() {
    int T,x1,x2,num;
    int matrix1[4][4] = {0};
    int matrix2[4][4] = {0};
    cin >> T;
    
    for (int i=0;i<T;++i) {
    	cin >> x1;
	for(int j=0;j<4;++j){
	    for(int k=0;k<4;++k) {
	    	cin >> matrix1[j][k];
	    }
	}
	cin >> x2;
	for(int j=0;j<4;++j){
	    for(int k=0;k<4;++k) {
	    	cin >> matrix2[j][k];
	    }
    	}
     int count = solve(matrix1,matrix2,x1,x2,&num);
     if(count == 0) cout << "Case #"<<i+1<<": Volunteer cheated!"<<endl;
     else if(count == 1) cout << "Case #" << i+1 << ": "<<num<<endl;
     else cout << "Case #" <<i+1 <<": Bad magician!"<<endl;
    }
    return 0;
}
