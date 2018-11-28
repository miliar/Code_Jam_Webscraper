#include <iostream>
#include<cstring>
#include<cstdio>
#define SIZE 1025
using namespace std;
int tree[SIZE];
void update(int idx,int val)
{
    while(idx < SIZE)
    {
        tree[idx]+=val;
        idx += (idx & -idx); // add the last non-zero digit
    }
}
int read(int idx)
{
    int sum = 0;
    while(idx > 0)
    {
        sum+=tree[idx];
        idx -= (idx & -idx); // deduct the last non-zero digit
    }
    return sum;
}
int main()
{
    int cas,n;
    char str[SIZE];
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    cin>>cas;
    for(int q=1;q<=cas;q++){
        memset(tree,false,sizeof(tree));
        bool impossible = false;
        int cnt = 0;
        cin>>str>>n;
        int len = strlen(str);
        for(int i=0;i<len;i++){
            if(i+n<=len){
                int flip = read(i+1);
                if((str[i] == '-' && flip%2==0) ||(str[i]=='+' &&flip%2==1)){
                    cnt++;
                    update(i+1,1);
                    update(i+1+n,-1);
                }
            }
            else{
                if( read(i+1)%2 == 0){
                    if(str[i]=='-')impossible = true;
                }
                else if(str[i]=='+')impossible = true;
            }
        }

        cout<<"Case #"<<q<<": ";
        if(impossible)cout<<"IMPOSSIBLE"<<endl;
        else cout<<cnt<<endl;
    }
    return 0;
}
