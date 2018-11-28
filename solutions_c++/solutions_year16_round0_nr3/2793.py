#include<bits/stdc++.h>
typedef long long LL;
using namespace std;
LL numbers[11];
LL digits[35];
LL numbersBase[35];
int n,j;
int cnt=0;
long long checkPrime(LL no)
{
    if(no&1){
        LL x=sqrt(no);
        for(LL i=3;i<=x;i+=2){
            if(no%i==0)return i;
        }
        return 0;
    }
    else{
        return 2;
    }
}
void possibleCombinations(int currIndex)
{

    //cout<<"inside\n";
    if(currIndex==n-1){
        LL base;
        for(base=2;base<=10;base++){
            //cout<<"base="<<base;
            LL num=0,power=1;
            for(int i=n-1;i>=0;i--){
                num+=power*digits[i];
                power*=base;
            }
            //cout<<"num="<<num<<endl;
            numbers[base]=num;
            numbersBase[base]=checkPrime(num);
            //cout<<"numbersBase[base]="<<numbersBase[base]<<endl;
            if(numbersBase[base]==0){
                //cout<<"no is prime\n";
                return;
            }
        }
        for(int i=0;i<=n-1;i++){
            cout<<digits[i];
        }
        cout<<" ";
        for(int base=2;base<=10;base++){
            cout<<numbersBase[base]<<" ";
        }
        cout<<endl;
        cnt++;
        return;
    }
    //cout<<"going to recurse\n";
    digits[currIndex]=0;
    if(cnt>=j){
        return;
    }
    possibleCombinations(currIndex+1);
    digits[currIndex]=1;
    if(cnt>=j){
        return;
    }
    possibleCombinations(currIndex+1);
}
int main()
{
    int t;
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("output.cpp","wt",stdout);
    cin>>t;
    for(int testCase=1;testCase<=t;testCase++){
        cin>>n>>j;
        digits[0]=digits[n-1]=1;
        cout<<"Case #"<<testCase<<":\n";
        cnt=0;
        possibleCombinations(1);
    }
    return 0;
}
