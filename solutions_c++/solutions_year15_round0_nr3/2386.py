//
//  main.cpp
//  code_jam_qualification_round
//
//  Created by hijackyan on 4/11/15.
//  Copyright (c) 2015 hackerrank. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int map[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
int nagate[4][4] = {{1, 1, 1, 1},{1, -1, 1, -1},{1, -1, -1, 1},{1, 1, -1, -1}};

int reverse_map[4][4] = {{}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
int reverse_nagate[4][4] = {{},{-1, 1, -1, 1},{-1, 1, 1, -1},{-1, -1, 1, 1}};

string temp;
long long l;
long long x;

bool check(long long i, char target, int & acc, int & negative)
{
    negative *= nagate[acc][temp[i%l] - 104];
    acc = map[acc][temp[i%l] - 104];
    if(negative == 1 && ((target - 104) == acc))
        return true;
    return false;
}
/*
bool recheck(int i, char target, int & acc, int & negative)
{
    //cout<<i<<" "<<acc<<" "<<negative<<endl;
    negative *= reverse_nagate[temp[i%l] - 104][acc];
    acc = reverse_map[temp[i%l] - 104][acc];
    //cout<<"after: "<<i<<" "<<acc<<" "<<negative<<endl;
    if(negative == 1 && ((target - 104) == acc))
        return true;
    return false;
}
*/

bool cal()
{
    long long r = (x > 4) ? 4: x;
    
    long long i = 0;
    int acc_i = 0;
    int negative_i = 1;
    for(i = 0; i < l*r; i++)
    {
        if(check(i, 'i', acc_i, negative_i))
           break;
    }
    if(i == l*r) return false;
    //cout<<"i: "<<i<<endl;
    long long j = i+1;
    int acc_j = 0;
    int negative_j = 1;
    for(; j <= i + l*r; j++)
    {
        if(check(j, 'j', acc_j, negative_j))
           break;
    }
    if(j > i + l*r) return false;
    if((j+1)/l >= x) return false;
    //cout<<"j: "<<j<<endl;

    long long k;
    int acc_k = 0;
    int negative_k = 1;
    for(k = (j%l) + 1; k < l; k++)
        check(k, 'k', acc_k, negative_k);
    x -= (1 + j/l);
    x %= 4;
    for(k = 0; k < l*x; k++)
        check(k, 'k', acc_k, negative_k);

    return (acc_k == 3 && negative_k == 1);
}
int main() {
    int T;
    cin>>T;
    int case_number = 1;
    while(T--)
    {
        int r;
        cin>>l;
        cin>>x;
        cin>>temp;
        cout<<"Case #"<<case_number++<<": ";
        if(cal())
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}
