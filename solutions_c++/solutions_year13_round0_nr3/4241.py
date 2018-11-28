#include<iostream>
#include<cmath>
#include<vector>
using namespace std;
bool oneDigit(long long num){
    return num>=0&&num<=9 ;
}

bool isPalUtil(long long num, long long *dupNum)
{
    if (oneDigit(num))
        return (num == (*dupNum) % 10);
 
    if (!isPalUtil(num/10, dupNum))
        return false;
    *dupNum /= 10;
    return (num % 10 == (*dupNum) % 10);
}


int main(){
    
    vector<long long> v;
    long long a, i, z;
    for(i=1;i<=10000000;i++){
        z = i;
        if(isPalUtil(z, &z)){
            
            a = i*i;
            if(isPalUtil(a,&a))
                {
                    v.push_back(i*i);
                    //cout<<i*i<<endl;
                }
        }
    }
    
            
    long long t,tt=0;;
    cin>>t;
    while(t--)
    {
        long long x,y;
        cin>>x>>y;
        int c =0;
        for(i=0;i<v.size();i++)
        {
            if(v[i]>=x && v[i]<=y)
                c++;
        }
        //cout<<l<<" "<<h;
        cout<<"Case #"<<++tt<<": "<<c<<endl;
    }
    return 0;
}
