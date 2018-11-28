#include<bits/stdc++.h>

using namespace std;

string str;
char x;
char h='+';
char s='-';
void flip(int n)
{
    if(str[0]==h)
        x=s;
    else
        x=h;
    for(int i=0;i<=n;i++)
        str[i]=x;
}
int main()
{
    freopen("inputxyzll.in","r",stdin);
    freopen("outputxyzll.txt","w",stdout);
    int i,ctr;
    int t;
    cin>>t;
    for(int cases=1;cases<=t;cases++)
    {
        printf("Case #%d: ",cases);
        cin>>str;
        int ctr=0;
        for(int i=1;i<str.length();i++){
        	if(str[i-1]!=str[i]){
                flip(i-1);
        		ctr++;
        	}
        }
        if(str[0]==s)
            ctr++;
        cout<<ctr<<endl;
    }
    return 0;
}
