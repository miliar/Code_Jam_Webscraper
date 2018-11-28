#include<iostream>
#include<vector>
using namespace std;
#define VAL 4
int main() {
int t;
cin>>t;
int l=0;
while(t--) {
l++;
int a1,a2,i,j,r1[VAL][VAL],r2[VAL][VAL];
cin>>a1;
for(i=0;i<VAL;i++) {
for(j=0;j<VAL;j++) {
cin>>r1[i][j];
}
}
cin>>a2;
for(i=0;i<VAL;i++) {
for(j=0;j<VAL;j++) {
cin>>r2[i][j];
}
}
int foundCount = 0;
int val = -1;
for(i=0;i<VAL;i++){
for(j=0;j<VAL;j++){
if(r1[a1-1][i]==r2[a2-1][j]) {
foundCount++; val=r1[a1-1][i];
}
}
}
if(foundCount==1) {
cout<<"Case #"<<l<<": "<<val;
} else if(foundCount>0) {
cout<<"Case #"<<l<<": Bad magician!";
} else {
cout<<"Case #"<<l<<": Volunteer cheated!";
}
cout<<endl;
}
return 0;
}
