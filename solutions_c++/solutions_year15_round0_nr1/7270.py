#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int te=0;te<t;te++){
    int num;
    string str;
    cin>>num>>str;
    vector<int>arr(num+1);
    for(int i=0;i<=num;i++){
        arr[i]=(str[i]-'0');
    }
    int sum=0;
    int avl=arr[0];
    for(int i=1;i<=num;i++){
        if(i>avl){
            sum+=i-avl;
            avl+=i-avl+arr[i];
        }
        else avl+=arr[i];
    }
    cout<<"Case #"<<te+1<<": "<<sum<<endl;
    }
}
