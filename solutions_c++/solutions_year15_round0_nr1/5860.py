#include<iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
ifstream fin("A-large.in");
ofstream fout("A-big.out");
string s;
int arr[1010];
int cnt=0,jaw=0,t,i,i2,ms,len,i3;
fin>>t;
for (i2=0;i2<t;i2++){
fin>>ms;
fin>>s;
fout<<"Case #"<<i2+1<<": ";
len=ms+1;
cnt=0;
jaw=0;
for(i3=0;i3<len;i3++){
    arr[i3]=int(s[i3])-48;
}
    for ( i=0;i<len;i++){
    if(cnt<i){
        jaw=jaw+i-cnt;
        cnt=cnt+i-cnt;
    }
    if(cnt>=i)
        cnt=cnt+arr[i];
    }
    fout<<jaw<<endl;
}

}
