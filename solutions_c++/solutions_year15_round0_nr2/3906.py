#include<iostream>
#include<limits.h>
#define MAX 1000

using namespace std;

int chef[100][MAX];

int func(int I, int max)
{
    int min_time = max;
    int tmp_time = 0;
    int tmp = chef[I][max], tmpmax;
    chef[I][max] = 0;
    for(tmpmax = max-1; tmpmax >= 0 && chef[I][tmpmax]==0; tmpmax--);
    for(int i = 2; i <= max/2; i++) {
        chef[I][i] += tmp;
        chef[I][max-i] += tmp;
        tmp_time = func(I, tmpmax>(max-i)?tmpmax:max-i) + tmp;
//        cout<<max<<i<<tmp_time<<endl;
        if(tmp_time < min_time)
            min_time = tmp_time;
        chef[I][i] -= tmp;
        chef[I][max-i] -= tmp;
    }
    chef[I][max] = tmp;

    return min_time;
}

int main()
{
    int T;
    cin>>T;

    int D;
    for(int i = 0; i < T; i++) {
        cin>>D;
        int tmp;
        int max = 0;
        for(int j = 0; j < D; j++) {
            cin>>tmp;
            chef[i][tmp]++;
            if(tmp>max)
                max = tmp;
        }
//        cout<<max<<endl;
        int res = func(i,max);
        cout<<"Case #"<<i+1<<": "<<res;
        if(i != T-1)
            cout<<endl;
    }

    return 0;
}
