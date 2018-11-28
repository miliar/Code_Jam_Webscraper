#include <bits/stdc++.h>

using namespace std;
int T;
int N[101];
bool digits[101][10];
bool isOK(int t){
    bool _flag = true;
    for(int i=0; i<10; i++)
    {
        if(!digits[t][i]) _flag = false;
    }
    return _flag;
}
void addToMatrix(int t, int sum){
    while(sum>0){
        digits[t][sum%10] = true;
        sum/=10;
    }
}
int main()
{
    ofstream file ("output.out");
    int i;
    cin>>T;
    for(i=0; i<T; i++)
    {
        cin>>N[i];
    }
    memset(digits,0,sizeof(digits));
    for(i=0; i<T; i++)
    {
        if(N[i]==0)
        {
            file<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        int lsum=1*N[i];
        addToMatrix(i,lsum);
        int multiplier = 2;
        while(!isOK(i)){
            lsum=N[i]*multiplier;
            addToMatrix(i,lsum);
            multiplier++;
        }
        file<<"Case #"<<i+1<<": "<<lsum<<endl;
    }
    return 0;
}
