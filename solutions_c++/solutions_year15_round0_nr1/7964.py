#include<vector>
#include<iostream>
#include<string>

using namespace std;

int main(){

int n, ppl;
string shy;

cin>>n;
for(int i=0;i<n;i++){
    
    int need=0 ,tempneed=0;
    cin>>ppl>>shy;
    //cout<<int(shy[0])<<"BB"<<endl;
    int standing=int(shy[0])-48;
    for(int j=1;j<=ppl;j++){
        tempneed=0;
        tempneed=max(0, j-standing);
        need+=tempneed;
        standing+=(int(shy[j])-48+tempneed);
     }
     cout<<"Case #"<<i+1<<": "<<need<<endl;
        

}

}