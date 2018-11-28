#include<iostream>
#include<fstream>
using namespace std;
int main() {
    int num;
    int n1,n2;
    int arr1[4][4];
    int arr2[4][4];
    int found = 0;
    int temp;
    ifstream file("A-small-attempt0.in");
    ofstream out("output.txt");
    file>>num;
    for(int i=0;i<num;i++) {
            file>>n1;
    for(int j=0;j<4;j++) {
    for(int k=0;k<4;k++) {
            file>>arr1[j][k];
            }}
    file>>n2;
    for(int j=0;j<4;j++) {
    for(int k=0;k<4;k++) {
            file>>arr2[j][k];
            }}
    for(int j=0;j<4;j++) {
    for(int k=0;k<4;k++) {
            if(arr1[n1-1][j]==arr2[n2-1][k]) {
            temp = arr1[n1-1][j];
            found++;
            }}}
    cout<<"Case #"<<i+1<<": ";
    if(found==1) cout<<temp;
    else if(found==0) cout<<"Volunteer cheated!";
    else if(found>0) cout<<"Bad magician!";
    cout<<endl;
    out<<"Case #"<<i+1<<": ";
    if(found==1) out<<temp;
    else if(found==0) out<<"Volunteer cheated!";
    else if(found>0) out<<"Bad magician!";
    out<<endl;
    found=0;
            }
            cout<<endl;
            //cin.get();
            file.close();
            out.close();
            return 0;
            }
            
