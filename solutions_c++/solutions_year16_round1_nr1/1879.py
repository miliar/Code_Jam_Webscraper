#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    long T,j=0;
    string S,last_word,temp1,temp2;
    cin>>T;
    while(T--){
        j++;
        cin>>S;
        last_word="";
        last_word+=S.at(0);
        for(int i=1;i<S.length();i++){
            temp1=last_word+S.at(i);
            temp2=S.at(i)+last_word;
            // cout<<temp1<<","<<temp2<<" " ;
            if(temp1.compare(temp2)>0)
                last_word=temp1;
            else
                last_word=temp2;
        }

        cout<<"Case #"<<j<<": "<<last_word<<endl;
    }
    
    return 0;
}