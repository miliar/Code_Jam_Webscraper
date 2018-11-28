#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    long T,j=0,alphabets[26],flag=0,number[10];
    string S,temp;
    string map[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    char c;
    cin>>T;
    while(T--){
        j++;
        cin>>S;
        long number[10]={0};
        long alphabets[26] = {0};
        long tempAlphabets[26] = {0};
        for(int i=0;i<S.length();i++){
            c=S.at(i);
            alphabets[c-65]++;
        }
        int pos=0;
        while(pos<10){
            temp=map[pos];
            flag=0;
            for(int i=0;i<26;i++)
                tempAlphabets[i]=alphabets[i];
            for(int j=0;j<temp.length();j++){
                c=temp.at(j);
                if(tempAlphabets[c-65]==0){
                    flag++;
                }
                else
                    tempAlphabets[c-65]--;  
            }
            if(flag==0){
                for(int i=0;i<26;i++)
                    alphabets[i]=tempAlphabets[i];
                number[pos]++;
            }
            else{
                //pos will go 0-2-4-6-8-1-3-5-7-9
                if(pos==8)
                    pos=1;
                else
                    pos=(pos+2);
            }
        }
        cout<<"Case #"<<j<<": ";
        for(int i=0;i<10;i++){
            while(number[i]){
                cout<<i;
                number[i]--;
            }
        }
        cout<<endl;
    }
    
    return 0;
}