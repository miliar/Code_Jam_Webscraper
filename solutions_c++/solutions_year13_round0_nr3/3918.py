#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
using namespace std;
int T;
int A;
int B;
int map[1000];
int count;
bool checkPalin(int num);
float InvSqrt(float x)
{
    float xhalf = 0.5f*x;
    int i = *(int*)&x;  
    i = 0x5f375a86- (i>>1); 
    x = *(float*)&i; 
    x = x*(1.5f-xhalf*x*x); 
    x = x*(1.5f-xhalf*x*x); 
    x = x*(1.5f-xhalf*x*x); 

    return 1/x;
}
void check(int num, int caseNum){
    double tmp = InvSqrt((double)num);
    if(fmod(tmp, 1)>0.00001){
//    if(num==4) cout<<tmp<<endl;
        return;
    }
    if(checkPalin(int(tmp))&&checkPalin(int(num))){
        count++;
        if((num*num)<=1000) map[num*num] = caseNum;
        return;
    }
    return;
}
bool checkPalin(int num){
    stringstream tmp;
    tmp << num;
    string in = tmp.str();
    if(in==string(in.rbegin(),  in.rend())){
        return true;
    }
    else{
        return false;
    }
}
void output(int num, int caseNum){
    cout<<"Case #"<<caseNum<<": "<<num<<endl;
    return;
}
int main(){
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>A;
        cin>>B;
        count = 0;
        for(int j=A;j<=B;j++){
            if(map[j]==i&&map[j]!=0) continue;
            else{
                check(j, i);
            }
        }
        output(count, i+1);
    }
  //  cout<<checkPalin(4)<<" "<<checkPalin(2)<<endl;
}
