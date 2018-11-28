#include<iostream>
#include<fstream>
using namespace std;
#define N 5

int judge(int f[N][N],int o,int s[N][N],int t,int* a)
{
    int pos = -1;
    for(int i = 1; i < N; i++)
        for(int j = 1; j < N; j++)
            if(f[o][j] == s[t][i])
            {
                (*a) = f[o][j];
                pos++;
            }
    return pos;
}

int main()
{
    ifstream cin("D:\\A-small-attempt0.in");
    ofstream cout("D:\\A-small-attempt0.out");
    int k;
    cin>>k;
    string ans[N]= {"Case #",": ","Bad magician!", "Volunteer cheated!"};
    for(int time = 1; time <= k; time++)
    {
        int first[N][N], second[N][N], one, two,pos,result;
        cin>>one;
        for(int i = 1; i <N ; i++)
            for(int j = 1; j <N ; j++)
                cin>>first[i][j];
        cin>>two;
        for(int i = 1; i <N ; i++)
            for(int j = 1; j <N ; j++)
                cin>>second[i][j];
        cout<<ans[0]<<time<<ans[1];
        pos = judge(first,one,second,two,&result);
        if(-1 == pos)
            cout<<ans[3];
        else
        {
            if(pos)
                cout<<ans[2];
            else
                cout<<result;
        }
        cout<<endl;

    }
    return 0;
}
