#include <iostream>
#include <vector>
#include <algorithm>
#include<string>
using namespace std;

vector<string> V;
int A[30];
int L;

void swap(int x, int y){
    string temp = V[x];
    V[x]=V[y];
    V[y]=temp;
    return;
}
void printV(int size){
    string s;
    bool c=true;
    for(int i=0; i<V.size(); i++)
    {
        s+=V[i];
    }
    int B[30];
    for(int i=0; i<30; i++)
        B[i]=0;
    for(int i=0; i<s.length()-1; i++)
    {
        B[ s[i]-97 ]++;
        if(s[i]!=s[i+1] && B[s[i]-97]<A[s[i]-97]) c=false;
    }
    if(c) L++;
    return;
}
void permute(int k,int size){
    int i;

    if (k==0)
        printV(size);
    else{
        for (i=k-1;i>=0;i--){
            swap(i,k-1);
            permute(k-1,size);
            swap(i,k-1);
        }
    }

    return;
}

int main () {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=0; tt<T; tt++)
    {
        int n;
        cin>>n;

        string s, z;
        string S="";
        L=0;
        for(int i=1; i<=n; i++)
        {
            cin>>s;
            z="";
            z+=s[0];
            for(int j=1; j<s.length(); j++)
                if(s[j]!=s[j-1]) z+=s[j];
            V.push_back(z);
            S+=z;
        }
        for(int i=0; i<30; i++)
            A[i]=0;
        for(int i=0; i<S.size(); i++)
            A[ S[i]-97 ]++;
        permute(n, n);
        cout<<"Case #"<<tt+1<<": "<<L<<endl;
        V.clear();
    }
    return 0;
}
