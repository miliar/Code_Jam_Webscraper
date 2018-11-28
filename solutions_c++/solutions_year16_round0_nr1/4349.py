#include <iostream>
#include <bits/stdc++.h>
using namespace std;


#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);
int visited[11];
int counter1=0;
void mark(int n)
{
    if(n%10==0)
    if(visited[0]==0){
            visited[0]=1;
            counter1++;
    }
    while(n!=0)
    {
        if(visited[n%10]==0){
        visited[n%10]=1;
        counter1++;
        }
        n=n/10;
    }
}

//int ans[201];
int main()
{
    READ("inputlarge.txt");
    WRITE("ouputlarge.txt");
    int t,flag=0;
    int n,counter=1;
    cin>>t;
    while(t--){
        flag=0;
        counter1=0;
        memset(visited, 0, sizeof visited);
        cin>>n;
        if(n==0){
            cout<<"Case #"<<counter<<": "<<"INSOMNIA"<<endl;
            counter++;
            continue;
            }
        int k=n;
        int i=2;
        while(k<=10000000)
        {

            mark(k);
            if(counter1==10)
            {
                flag=1;
                break;
            }
            k=i*n;
            i++;

        }
        if(flag==1)
        {
            cout<<"Case #"<<counter<<": "<<k<<endl;
        }
        else{
            cout<<"Case #"<<counter<<": "<<"INSOMNIA"<<endl;
        }
        counter++;

    }

    return 0;
}
