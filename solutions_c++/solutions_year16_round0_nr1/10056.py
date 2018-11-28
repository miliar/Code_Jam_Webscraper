//
// Created by smalldog on 16/4/10.
//

#include "1.h"
//
// Created by smalldog on 16/4/9.
//

#include "1.h"
#include<iostream>
#include<vector>

using namespace std;

bool Judge(vector<int> a)
{
    for(int i=0;i<a.size();i++)
    {
        if(a[i]==0)
            return false;
    }
    return true;
}

int Counting(int tmp)
{

    int N=tmp;
    int i=1;
    vector<int> a(10);
    if(N==0)
        return 0;
    while(1)
    {
        N=N*i;
        int tmp1=N;
        while(tmp1!=0)
        {
            int tmp2=tmp1%10;
            a[tmp2]=1;
            tmp1=tmp1/10;


        }
        if(Judge(a))
        {
            return N;

        }

    }

}

int main()
{
    int T;
    int N;
    vector<int> input;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>N;
        input.push_back(N);
    }
    for(int i=0;i<T;i++)
    {
        int tmp=input[i];
        int res=Counting(tmp);
    }



}

