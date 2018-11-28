#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int t;
int n;

int solve(string str){

    int i;

    string temp = "";
    temp += str[0];

    bool flag = false;

    for (i=1;i<str.size();i++){
        if (str[i] != str[0]){
            flag = true;
            break;
        } else {
            temp += str[i];
        }
    }

    if (!flag){
        if (str[0] == '-'){
            return 1;
        } else {
            return 0;
        }
    }

    string new_temp = "";

    for (int i=temp.size()-1; i >= 0; i--){
        if (temp[i] == '-'){
            new_temp += '+';
        } else {
            new_temp += '-';
        }
    }

    for (int i=0; i!= new_temp.size(); i++){
        str[i] = new_temp[i];
    }

    return solve(str) + 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data11.txt","w",stdout);

    scanf("%i",&t);

    for (int j=1; j <= t; j++){


        char temp[101];
        scanf("%100s",temp);

        printf("Case #%i: ",j);

        string tempp = temp;


        printf("%i\n",solve(tempp));
    }
}
