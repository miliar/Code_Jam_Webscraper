#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int t;
int n;

bool nums[10];

void init(){
    for (int i=0; i!= 10; i++){
        nums[i] = false;
    }
}

string str(long long int num){
    stringstream ss;
    ss << num;
    return ss.str();
}

long long int turns;

bool solve(long long int num){

    turns++;

    string temp = str(num);

    for (int i=0; i!= temp.size(); i++){
        nums[temp[i] - '0'] = true;
    }

    bool yes = true;

    for (int i=0; i!= 10; i++){
        if (!nums[i]){
            yes = false;
        }
    }

    if (yes){
        return true;
    }

    if (num == (num/turns) * (turns+1)){
        return false;
    }

    solve((num/turns) * (turns+1));
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data2.txt","w",stdout);

    scanf("%i",&t);

    for (int j=1; j<=t; j++){

        init();

        turns = 0;

        scanf("%i",&n);
        printf("Case #%i: ",j);

        long long int temp = n;
        if (solve(n)){
            printf("%I64d\n",turns*n);
        } else {
            printf("INSOMNIA\n");
        }
    }

    return (0);


}
