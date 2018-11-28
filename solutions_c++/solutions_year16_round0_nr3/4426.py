#include<bits/stdc++.h>
using namespace std;
long long x,a,b,ans[101],cnt,base,yes[11],c,ds;
string s[101];
bool y,flag;
map<long long,long long>arr;
void tot(int z,string d){
if(c==0)return;
else if(d.size()==z){
        flag=false;
    for(int i=2;i<=10;i++){
            cnt=1;
            base=i;
        for(int j=d.size()-1;j>=0;j--){
            //cout<<d[j]-48;
            cnt+=((d[j]-48)*base);
            //cout<<cnt<<endl;
            base*=i;
        }
        cnt+=base;
        //cout<<d<<" "<<cnt<<endl;
        //if(i==10)cout<<d<<" "<<cnt<<endl;
        ds=-1;
        for(long long j=2;j*j<=cnt;j++){
            if(cnt%j==0){
                ds=j;
                break;
            }
        }
        if(ds!=-1)yes[i]=ds;
        else{
            flag=true;
            break;
        }
    }
    if(!flag){
        cout<<"1"<<d<<"1 ";
       for(int i=2;i<=10;i++)cout<<yes[i]<<" ";
        cout<<endl;
        c--;
    }
    return;
}
tot(z,d+'0');
tot(z,d+'1');
return;
}
int main(){
 // ifstream m;
  //m.open ("C-small-attempt0.in");
 // ofstream f;
  //f.open("output.txt");
 cin>>x;
// m>>x;
 for(int i=0;i<x;i++){
    cin>>a>>b;
  // m>>a>>b;
 }
/*for (int i=2; i<1000001; i++){
        for (int j=2; j*j<=i; j++){
            if (i%j==0){
                arr[i]=j;
                break;
            }
            else if(j+1>sqrt(i)) {
                arr[i]=-1;
            }
        }
}*/
c=b;
cout<<"Case #1:"<<endl;
tot(a-2,"");
}
