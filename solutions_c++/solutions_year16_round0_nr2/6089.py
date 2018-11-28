#include<iostream>
#include<cstdio>
#define gc getchar
using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main(){

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int test,t=0,i,count;
    string str;
    scanint(test);

    while(t<test){
        cin>>str;
        i=0;
        count=0;
        while(i<str.length()-1){
            if(str[i]!=str[i+1])
                count++;
            i++;
        } 
        if(str[i]=='-')
        	cout<<"Case #"<<t+1<<": "<<count+1<<endl;
        else
            cout<<"Case #"<<t+1<<": "<<count<<endl;
        t++;
    }

return 0;
}
