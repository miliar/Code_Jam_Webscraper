#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int check(string s1, string s2){
    int i, j;
    j = 0;
    int count = 0;
    for(i = 0; i< s1.size() && j<s2.size(); ){
        //cout<<s1[i]<<","<<s2[j]<<endl;
        if(s1[i] == s2[j]){
            j++;
            i++;
        }
        else if( j > 0 && s2[j] == s2[j-1]){
            count++;
            j++;
        }
        else if( i > 0 && s1[i] == s1[i-1]){
            count++;
            i++;
        }
        else{
            return -1;
        }
    }
    if(i==s1.size()) {
        for(;j<s2.size(); j++){
            if(s2[j] == s2[j-1])  count++;
            else return -1;
        }
    }
    if(j==s2.size()) {
        for(;i<s1.size(); i++){
            if(s1[i] == s1[i-1])  count++;
            else return -1;
        }
    }

    return count;
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
	freopen("out4.txt", "w", stdout);
    int t;
    char str1[101], str2[101];
    scanf("%d\n",&t);
    string *s1, *s2;

    for (int z = 0; z<t; z++){
        int n;
        scanf("%d\n",&n);

        gets(str1);
        gets(str2);

        s1 = new string(str1);
        s2 = new string(str2);
        int count;
        if(s1->size() < s2->size()) {
           count = check(*s1, *s2) ;
        }
        else {
            count = check(*s2, *s1);
        }

        cout<<"Case #"<<z+1<<": ";
        if(count == -1){
            cout<<"Fegla Won"<<endl;
        }
        else {
            cout<<count<<endl;
        }
    }
    return 0;
}
