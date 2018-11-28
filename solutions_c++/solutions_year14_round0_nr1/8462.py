#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main(void){


   int T,N;
   bool a[16], b[16];
   cin >> T;
   for (int k=0; k< T; k++) {
   	 int N, M;
   	 cin >> N;
   	 for(int i=0;i<4;i++){
   	 	for(int j=0;j<4;j++){
   	 		int temp;
   	 		cin>>temp;
   	 		a[temp-1] = 0;
   	 		if(i==N-1){
   	 			a[temp-1] = 1;
   	 			// cout <<temp << " ";
   	 		}
   	 	}
   	 }

   	 cin >> M;
   	 for(int i=0;i<4;i++){
   	 	for(int j=0;j<4;j++){
   	 		int temp;
   	 		cin>>temp;
   	 		b[temp-1] = 0;
   	 		if(i==M-1){
   	 			b[temp-1] = 1;
   	 			// cout <<temp << " ";
   	 		}
   	 	}
   	 }
   	 bool check = false;
   	 int n;
   	 int flag = false;
   	 cout << "CASE #" << k+1 <<": ";
   	 for(int i=0;i<16;i++){
   	 	if(a[i] && b[i] && !check){
   	 		check = true;
   	 		n = i + 1;
   	 	}
   	 	else if(a[i] && b[i] && check){
   	 		cout << "Bad magician!"<<endl;
   	 		flag = true;
   	 		break;
   	 	}
   	 }
   	 if(flag) continue;
   	 if(!check){
   	 	cout << "Volunteer cheated!" <<endl;
   	 }
   	 else{
   	 	cout << n <<endl;
   	 }
   }
   return 0;
}
