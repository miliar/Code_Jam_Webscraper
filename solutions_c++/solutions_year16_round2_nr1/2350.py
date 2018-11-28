#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<cstdlib>
#include<map>
#include<cstdio>
#include<cmath>
#include<queue>
#include<algorithm>
using namespace std;
int data[28];
int main(){
    string str;
    vector<int>result;
 //   freopen("input.txt","r",stdin);
   //freopen("output.txt","w",stdout);
    int i,testcase,j,a,b;
    scanf("%d",&testcase);
    for( i = 1; i <= testcase; i++ ){

        for( j = 0; j <= 26 ; j++){
            data[j] = 0;
        }
        cin>>str;
        for( j = 0; j < str.size(); j++){
            a = str[j] - 'A';
            data[a]++;
        }
        b = 'Z' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(0);
            a = 'E' - 'A';
            data[a]--;
            a = 'R' - 'A';
            data[a]--;
            a = 'O' - 'A';
            data[a]--;
        }
        b = 'G' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(8);
            a = 'E' - 'A';
            data[a]--;
            a = 'I' - 'A';
            data[a]--;
            a = 'H' - 'A';
            data[a]--;
            a = 'T' - 'A';
            data[a]--;
        }
        b = 'X' - 'A';
         for( j = 1; j <= data[b]; j++){
            result.push_back(6);
            a = 'S' - 'A';
            data[a]--;
            a = 'I' - 'A';
            data[a]--;
        }
        b = 'S' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(7);
            a = 'E' - 'A';
            data[a]--;
            a = 'V' - 'A';
            data[a]--;
            a = 'E' - 'A';
            data[a]--;
            a = 'N' - 'A';
            data[a]--;
        }

        b = 'V' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(5);
            a = 'F' - 'A';
            data[a]--;
            a = 'I' - 'A';
            data[a]--;
            a = 'E' - 'A';
            data[a]--;
        }
        b = 'F' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(4);
            a = 'O' - 'A';
            data[a]--;
            a = 'U' - 'A';
            data[a]--;
            a = 'R' - 'A';
            data[a]--;
        }
        b = 'R' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(3);
            a = 'T' - 'A';
            data[a]--;
            a = 'H' - 'A';
            data[a]--;
            a = 'E' - 'A';
            data[a]--;
            a = 'E' - 'A';
            data[a]--;
        }
        b = 'W' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(2);
            a = 'O' - 'A';
            data[a]--;
            a = 'T' - 'A';
            data[a]--;
        }
        b = 'I' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(9);
            a = 'N' - 'A';
            data[a]--;
            a = 'N' - 'A';
            data[a]--;
            a = 'E' - 'A';
            data[a]--;
        }
        b = 'O' - 'A';
        for( j = 1; j <= data[b]; j++){
            result.push_back(1);
        }
        printf("Case #%d: ",i);
        sort(result.begin(),result.end());
        for( j = 0; j < result.size(); j++ ){
            cout<<result[j];
        }
        cout<<endl;
        result.clear();

    }



return 0;
}
