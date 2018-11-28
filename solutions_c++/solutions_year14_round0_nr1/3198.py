#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdin(0);cin.tie(0);
using namespace std;
int N, r, ar[4][4], arr[4][4], ro[4], row[4]; vector<int> sam;
int main(){ cin >> N;
for(int M=1; M<=N; M++){
cin >> r;
for (int i=0; i<4;i++){
for(int j=0; j<4; j++){cin>>ar[i][j]; if(r-1==i){ro[j]=ar[i][j];}}}
cin >> r;
for (int i=0; i<4;i++){
for(int j=0; j<4; j++){cin>>arr[i][j]; if(r-1==i){row[j]=arr[i][j];}}} sam.clear();
for (int i=0; i<4; i++){for(int j=0;j<4;j++){if(ro[i]==row[j]){sam.push_back(ro[i]); }}}
cout << "Case #" << M << ": "; 
if ((int)sam.size()==0) cout <<"Volunteer cheated!" << endl; 
else if((int)sam.size()==1) cout << sam[0] << endl;
else cout<< "Bad magician!"<<endl;
}return 0;}